import torch
import torch.nn.functional as F
import torch.nn as nn
import math
import importlib
from pathlib import Path

import nodes

blending_modes = {
    'add': lambda a, b, factor: (a * factor + b * factor),
    'bislerp': lambda a, b, t: normalize((1 - t) * a + t * b),
    'color dodge': lambda a, b, factor: a / (1 - b + 1e-6),
    'cosine interp': lambda a, b, t: (a + b - (a - b) * torch.cos(t * torch.tensor(math.pi))) / 2,
    'cuberp': lambda a, b, t: a + (b - a) * (3 * t ** 2 - 2 * t ** 3),
    'difference': lambda a, b, factor: normalize(abs(a - b) * factor),
    'exclusion': lambda a, b, factor: normalize((a + b - 2 * a * b) * factor),
    'glow': lambda a, b, factor: torch.where(a <= 1, a ** 2 / (1 - b + 1e-6), b * (a - 1) / (a + 1e-6)),
    'hard light': lambda a, b, factor: (2 * a * b * (a < 0.5).float() + (1 - 2 * (1 - a) * (1 - b)) * (a >= 0.5).float()) * factor,
    'lerp': lambda a, b, t: (1 - t) * a + t * b,
    'linear dodge': lambda a, b, factor: normalize(a + b * factor),
    'linear light': lambda a, b, factor: torch.where(b <= 0.5, a + 2 * b - 1, a + 2 * (b - 0.5)),
    'multiply': lambda a, b, factor: normalize(a * factor * b * factor),
    'overlay': lambda a, b, factor: (2 * a * b + a**2 - 2 * a * b * a) * factor if torch.all(b < 0.5) else (1 - 2 * (1 - a) * (1 - b)) * factor,
    'pin_light': lambda a, b, factor: torch.where(b <= 0.5, torch.min(a, 2 * b), torch.max(a, 2 * b - 1)),
    'random': lambda a, b, factor: normalize(torch.rand_like(a) * a * factor + torch.rand_like(b) * b * factor),
    'reflect': lambda a, b, factor: torch.where(b <= 1, b ** 2 / (1 - a + 1e-6), a * (b - 1) / (b + 1e-6)),
    'screen': lambda a, b, factor: normalize(1 - (1 - a) * (1 - b) * (1 - factor)),
    'slerp': lambda a, b, t: normalize(((a * torch.sin((1 - t) * torch.acos(torch.clamp(torch.sum(a * b, dim=1), -1.0, 1.0))) + b * torch.sin(t * torch.acos(torch.clamp(torch.sum(a * b, dim=1), -1.0, 1.0)))) / torch.sin(torch.acos(torch.clamp(torch.sum(a * b, dim=1), -1.0, 1.0))))),
    'subtract': lambda a, b, factor: (a * factor - b * factor),
    'vivid light': lambda a, b, factor: torch.where(b <= 0.5, a / (1 - 2 * b + 1e-6), (a + 2 * b - 1) / (2 * (1 - b) + 1e-6)),
}

def normalize(latent, target_min=None, target_max=None):
    min_val = latent.min()
    max_val = latent.max()
    
    if target_min is None:
        target_min = min_val
    if target_max is None:
        target_max = max_val
        
    normalized = (latent - min_val) / (max_val - min_val)
    scaled = normalized * (target_max - target_min) + target_min
    return scaled

def create_gaussian_kernel(k_size, sigma):
    """Create a 2D Gaussian kernel."""
    kernel = torch.tensor([[math.exp(-((i - k_size[0] // 2) ** 2 + (j - k_size[1] // 2) ** 2) / (2 * sigma ** 2))
                            for j in range(k_size[1])]
                           for i in range(k_size[0])])
    kernel = kernel / kernel.sum()
    return kernel

def generate_noise_map(width, height, X, Y, Z, frame, device, evolution, octaves, persistence, lacunarity, exponent, scale, brightness, contrast, seed, clamp_min, clamp_max):

        PPF = PerlinPowerFractal(width, height)
        noise_map = PPF(1, X, Y, Z, frame, device, evolution, octaves, persistence, lacunarity, exponent, scale, brightness, contrast, seed, clamp_min, clamp_max)
        return noise_map

def power_fractal_latent(batch_size, width, height, resampling, X, Y, Z, evolution, frame, scale, octaves, persistence, lacunarity, exponent, brightness, contrast, clamp_min, clamp_max, seed, device, optional_vae=None):
                    
        color_intensity = 1
        masking_intensity = 1
        
        batch_size = int(batch_size)
        width = int(width)
        height = int(height)

        channel_tensors = []
        for i in range(batch_size):
            nseed = seed + i * 12
            rgb_noise_maps = []
            
            rgb_image = torch.zeros(4, height, width)
            
            for j in range(3):
                rgba_noise_map = generate_noise_map(width, height, X, Y, Z, frame, device, evolution, octaves, persistence, lacunarity, exponent, scale, brightness, contrast, nseed + j, clamp_min, clamp_max)
                rgb_noise_map = rgba_noise_map.squeeze(-1)
                rgb_noise_map *= color_intensity
                rgb_noise_map *= masking_intensity
                
                rgb_image[j] = rgb_noise_map
                
            rgb_image[3] = torch.ones(height, width)
            
            channel_tensors.append(rgb_image)
            
        tensors = torch.stack(channel_tensors)
        tensors = normalize(tensors)
        
        if optional_vae is None:
            latents = F.interpolate(tensors, size=((height // 8), (width // 8)), mode=resampling)
            return {'samples': latents}, tensors.permute(0, 2, 3, 1)
            
        encoder = nodes.VAEEncode()
        
        latents = []
        for tensor in tensors:
            tensor = tensor.unsqueeze(0)
            tensor = tensor.permute(0, 2, 3, 1)
            latents.append(encoder.encode(optional_vae, tensor)[0]['samples'])
            
        latents = torch.cat(latents)
        
        return {'samples': latents}, tensors.permute(0, 2, 3, 1)


def cross_hatch(batch_size, width, height, resampling, frequency, octaves, persistence, color_tolerance, num_colors, angle_degrees, brightness, contrast, blur, clamp_min, clamp_max, seed, device, optional_vae=None):

        cross_hatch = CrossHatchPowerFractal(width=width, height=height, frequency=frequency, octaves=octaves, persistence=persistence, num_colors=num_colors, color_tolerance=color_tolerance, angle_degrees=angle_degrees, blur=blur, clamp_min=clamp_min, clamp_max=clamp_max)
        tensors = cross_hatch(batch_size, device, seed).to(device="cpu")
        tensors = torch.cat([tensors, torch.ones(batch_size, height, width, 1, dtype=tensors.dtype, device='cpu')], dim=-1)
                
        if optional_vae is None:
            latents = tensors.permute(0, 3, 1, 2)
            latents = F.interpolate(latents, size=((height // 8), (width // 8)), mode=resampling)
            return {'samples': latents}, tensors
            
        encoder = nodes.VAEEncode()
        
        latents = []
        for tensor in tensors:
            tensor = tensor.unsqueeze(0)
            latents.append(encoder.encode(optional_vae, tensor)[0]['samples'])
            
        latents = torch.cat(latents)
        
        return {'samples': latents}, tensors

class PerlinPowerFractal(nn.Module):
    """
    Generate a batch of images with a Perlin power fractal effect.

    Args:
        width (int): Width of each tensor in pixels. Range: [64, 8192].
        height (int): Height of each image in pixels. Range: [64, 8192].
        batch_size (int): Number of noisy tensors to generate in the batch. Range: [1, 64].
        X (float): X-coordinate offset for noise sampling. Range: [-99999999, 99999999].
        Y (float): Y-coordinate offset for noise sampling. Range: [-99999999, 99999999].
        Z (float): Z-coordinate offset for noise sampling. Range: [-99999999, 99999999].
        frame (int): The current frame number for time evolution. Range: [0, 99999999].
        evolution_factor (float): Factor controlling time evolution. Determines how much the noise evolves over time based on the batch index. Range: [0.0, 1.0].
        octaves (int): Number of octaves for fractal generation. Controls the level of detail and complexity in the output. Range: [1, 8].
        persistence (float): Persistence parameter for fractal generation. Determines the amplitude decrease of each octave. Range: [0.01, 23.0].
        lacunarity (float): Lacunarity parameter for fractal generation. Controls the increase in frequency from one octave to the next. Range: [0.01, 99.0].
        exponent (float): Exponent applied to the noise values. Adjusting this parameter controls the overall intensity and contrast of the output. Range: [0.01, 38.0].
        scale (float): Scaling factor for frequency of noise. Larger values produce smaller, more detailed patterns, while smaller values create larger patterns. Range: [2, 2048].
        brightness (float): Adjusts the overall brightness of the generated noise.
            - -1.0 makes the noise completely black.
            - 0.0 has no effect on brightness.
            - 1.0 makes the noise completely white. Range: [-1.0, 1.0].
        contrast (float): Adjusts the contrast of the generated noise.
            - -1.0 reduces contrast, enhancing the difference between dark and light areas.
            - 0.0 has no effect on contrast.
            - 1.0 increases contrast, enhancing the difference between dark and light areas. Range: [-1.0, 1.0].
        seed (int, optional): Seed for random number generation. If None, uses random seeds for each batch. Range: [0, 0xffffffffffffffff].

    Returns:
        torch.Tensor: A tensor containing the generated images in the shape (batch_size, height, width, 1).
    """
    def __init__(self, width, height):
        super(PerlinPowerFractal, self).__init__()
        self.width = width
        self.height = height

    def forward(self, batch_size, X, Y, Z, frame, device='cpu', evolution_factor=0.1,
                octaves=4, persistence=0.5, lacunarity=2.0, exponent=4.0, scale=100,
                brightness=0.0, contrast=0.0, seed=None, min_clamp=0.0, max_clamp=1.0):

        def fade(t):
            return 6 * t ** 5 - 15 * t ** 4 + 10 * t ** 3

        def lerp(t, a, b):
            return a + t * (b - a)

        def grad(hash, x, y, z):
            h = hash & 15
            u = torch.where(h < 8, x, y)
            v = torch.where(h < 4, y, torch.where((h == 12) | (h == 14), x, z))
            return torch.where(h & 1 == 0, u, -u) + torch.where(h & 2 == 0, v, -v)

        def noise(x, y, z, p):
            X = (x.floor() % 255).to(torch.int32)
            Y = (y.floor() % 255).to(torch.int32)
            Z = (z.floor() % 255).to(torch.int32)

            x -= x.floor()
            y -= y.floor()
            z -= z.floor()

            u = fade(x)
            v = fade(y)
            w = fade(z)

            A = p[X] + Y
            AA = p[A] + Z
            AB = p[A + 1] + Z
            B = p[X + 1] + Y
            BA = p[B] + Z
            BB = p[B + 1] + Z

            r = lerp(w, lerp(v, lerp(u, grad(p[AA], x, y, z), grad(p[BA], x - 1, y, z)),
                              lerp(u, grad(p[AB], x, y - 1, z), grad(p[BB], x - 1, y - 1, z))),
                     lerp(v, lerp(u, grad(p[AA + 1], x, y, z - 1), grad(p[BA + 1], x - 1, y, z - 1)),
                              lerp(u, grad(p[AB + 1], x, y - 1, z - 1), grad(p[BB + 1], x - 1, y - 1, z - 1))))

            return r

        device = 'cuda' if device == 'cuda' and torch.cuda.is_available() else 'cpu'

        unique_seed = seed if seed is not None else torch.randint(0, 10000, (1,)).item()
        torch.manual_seed(unique_seed)

        p = torch.randperm(max(self.width, self.height) ** 2, dtype=torch.int32, device=device)
        p = torch.cat((p, p))

        noise_map = torch.zeros(batch_size, self.height, self.width, dtype=torch.float32, device=device)

        X = torch.arange(self.width, dtype=torch.float32, device=device).unsqueeze(0).unsqueeze(0) + X
        Y = torch.arange(self.height, dtype=torch.float32, device=device).unsqueeze(1).unsqueeze(0) + Y
        Z = evolution_factor * torch.arange(batch_size, dtype=torch.float32, device=device).unsqueeze(1).unsqueeze(1) + Z + frame

        for octave in range(octaves):
            frequency = lacunarity ** octave
            amplitude = persistence ** octave

            nx = X / scale * frequency
            ny = Y / scale * frequency
            nz = (Z + frame * evolution_factor) / scale * frequency

            noise_values = noise(nx, ny, nz, p) * (amplitude ** exponent)

            noise_map += noise_values.squeeze(-1) * amplitude

        noise_map = normalize(noise_map, min_clamp, max_clamp)

        latent = (noise_map + brightness) * (1.0 + contrast)
        latent = normalize(latent)
        latent = latent.unsqueeze(-1)

        return latent
    
class CrossHatchPowerFractal(nn.Module):
    """
    Generate a batch of crosshatch-patterned images with a power fractal effect.

    Args:
        width (int): Width of each image in pixels.
        height (int): Height of each image in pixels.
        frequency (int, optional): Frequency of the crosshatch pattern. Default is 320.
        octaves (int, optional): Number of octaves for fractal generation. Controls the level of detail and complexity in the output. Default is 12.
        persistence (float, optional): Persistence parameter for fractal generation. Determines the amplitude decrease of each octave. Default is 1.5.
        num_colors (int, optional): Number of colors to map the generated noise to. Default is 16.
        color_tolerance (float, optional): Color tolerance for mapping noise values to colors. Default is 0.05.
        angle_degrees (float, optional): Angle in degrees for the crosshatch pattern orientation. Default is 45.
        blur (int, optional): Amount of blur to apply to the generated image. Default is 2.
        brightness (float, optional): Adjusts the overall brightness of the generated images. Default is 0.0.
        contrast (float, optional): Adjusts the contrast of the generated images. Default is 0.0.
        clamp_min (float, optional): Minimum value to clamp the pixel values to. Default is 0.0.
        clamp_max (float, optional): Maximum value to clamp the pixel values to. Default is 1.0.

    Returns:
        torch.Tensor: A tensor containing the generated images in the shape (batch_size, height, width, 3).
    """
    def __init__(self, width, height, frequency=320, octaves=12, persistence=1.5, num_colors=16, color_tolerance=0.05, angle_degrees=45, blur=2, brightness=0.0, contrast=0.0, clamp_min=0.0, clamp_max=1.0):
        super(CrossHatchPowerFractal, self).__init__()
        self.width = width
        self.height = height
        self.frequency = frequency
        self.num_octaves = octaves
        self.persistence = persistence
        self.angle_radians = math.radians(angle_degrees)
        self.num_colors = num_colors
        self.color_tolerance = color_tolerance
        self.blur = blur
        self.brightness = brightness
        self.contrast = contrast
        self.clamp_min = clamp_min
        self.clamp_max = clamp_max

    def forward(self, batch_size=1, device='cpu', seed=1):
        device_index = [torch.cuda.current_device()] if device.startswith('cuda') else None

        with torch.random.fork_rng(devices=device_index):
            x = torch.linspace(0, 1, self.width, dtype=torch.float32, device=device)
            y = torch.linspace(0, 1, self.height, dtype=torch.float32, device=device)
            x, y = torch.meshgrid(x, y, indexing="ij")

            batched_noises = []

            for i in range(batch_size):
                batch_seed = int(seed + i)
                noise = torch.zeros(self.width, self.height, device=device)

                for octave in range(self.num_octaves):
                    frequency = self.frequency * 2 ** octave
                    octave_noise = self.generate_octave(x, y, frequency)
                    noise += octave_noise * self.persistence ** octave

                noise = (noise - noise.min()) / (noise.max() - noise.min())
                colored_noise = self.apply_color_mapping(noise, device, batch_seed)
                colored_noise = colored_noise.cpu()

                r_channel = colored_noise[:, :, 0]
                g_channel = colored_noise[:, :, 1]
                b_channel = colored_noise[:, :, 2]

                kernel_size = int(self.blur * 2 + 1)
                uniform_kernel = torch.ones(1, 1, kernel_size, kernel_size) / (kernel_size * kernel_size)

                blurred_r = F.conv2d(r_channel.unsqueeze(0).unsqueeze(0), uniform_kernel, padding=int(self.blur))
                blurred_g = F.conv2d(g_channel.unsqueeze(0).unsqueeze(0), uniform_kernel, padding=int(self.blur))
                blurred_b = F.conv2d(b_channel.unsqueeze(0).unsqueeze(0), uniform_kernel, padding=int(self.blur))
                blurred_noise = torch.cat((blurred_r, blurred_g, blurred_b), dim=1)
                blurred_noise = F.interpolate(blurred_noise, size=(self.height, self.width), mode='bilinear')

                batched_noises.append(blurred_noise.permute(0, 2, 3, 1))

            batched_noises = torch.cat(batched_noises, dim=0).to(device='cpu')
            batched_noises = (batched_noises + self.brightness) * (1.0 + self.contrast)
            
            return normalize(batched_noises, self.clamp_min, self.clamp_max)

    def generate_octave(self, x, y, frequency):
        grid_hatch_x = torch.sin(x * frequency * math.pi)
        grid_hatch_y = torch.sin(y * frequency * math.pi)

        grid_hatch_x = (grid_hatch_x - grid_hatch_x.min()) / (grid_hatch_x.max() - grid_hatch_x.min())
        grid_hatch_y = (grid_hatch_y - grid_hatch_y.min()) / (grid_hatch_y.max() - grid_hatch_y.min())
        grid_hatch = grid_hatch_x + grid_hatch_y

        return grid_hatch

    def apply_color_mapping(self, noise, device, seed):
        generator = torch.Generator(device=device)
        generator.manual_seed(seed)
        random_colors = torch.rand(self.num_colors, 3, generator=generator, dtype=torch.float32, device=device)

        noise_scaled = noise * (self.num_colors - 1)
        tolerance = self.color_tolerance * (self.num_colors - 1)
        noise_scaled_rounded = torch.round(noise_scaled)
        colored_noise = random_colors[noise_scaled_rounded.long()]

        return colored_noise