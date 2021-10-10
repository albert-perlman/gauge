[Install](#install)<br/>
[Run](#run)<br/>
[Settings](#settings)<br/>

# gauge
Nvidia GPU temperature gauge widget with configurable colors and alarm temperature.<br/><br/>
![image](https://user-images.githubusercontent.com/53355129/136690624-30ad959a-8462-4b5a-afce-34c2d7ec0864.png)
![image](https://user-images.githubusercontent.com/53355129/136690535-1bd65d73-406f-4344-97c4-fb0ebecd5b41.png)<br/>
*designed for 2560x1440 resolution

## Install
[Windows 10 installer](https://github.com/albert-perlman/gauge/blob/main/target/gaugeSetup.exe)

## Run
`C:\Program Files (x86)\gauge\gauge.exe`

## Settings
Edit `C:\Program Files (x86)\gauge\gauge.config`
```
50,50
255,255,255,255
80
255,55,55,255

1. window position: (x,y) pixel coordinates
2. gauge color: red,green,blue,alpha
3. alarm temperature: degrees celcius
4: alarm indicator color: red,green,blue,alpha
```
