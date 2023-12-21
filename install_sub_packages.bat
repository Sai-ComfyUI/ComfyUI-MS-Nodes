git clone


IF NOT EXIST packages/ms_ZoeDepth (
    git clone http://gitlab.moonshine.tw/ai/custom_packages/ms_ZoeDepth packages/ms_ZoeDepth
    
) ELSE (

)

IF NOT EXIST packages/ms_MiDaS (
    git clone http://gitlab.moonshine.tw/ai/custom_packages/ms_ZoeDepth packages/ms_MiDaS
    
) ELSE (

)