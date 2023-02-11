
@ECHO OFF
set ROOT_PATH=%~dp0
@REM set SCRIPT_PATH=E:\ProgramData\Anaconda3\envs\tools\python.exe %ROOT_PATH%..\Scripts\baseyun.py
set SCRIPT_PATH=%ROOT_PATH%..\kernel\python.exe %ROOT_PATH%..\Scripts\baseyun.py

@IF [%1] == [activate] (
    if "%2" == "" (
        echo ERROR: No environment specified.
        exit /b 1
    )

    if DEFINED NOW_ENV (
        if "%NOW_ENV%" == "%2" (
            echo Environment already activated: %2
            exit /b 0
        )
    )

    
    del /f /q %ROOT_PATH%baseyun.tmp
    %SCRIPT_PATH% show --name %2 --do var --out %ROOT_PATH%baseyun.tmp> nul
    set /p RESULT=<%ROOT_PATH%baseyun.tmp


    echo %RESULT% | findstr ; >nul && echo '' || (
        echo ERROR: Activate environment failed
        echo If you think this is a bug, please retry
        exit /b 1
    )

    @REM 修改环境变量
    set PATH=%RESULT%
    set RESULT=
    @set "PROMPT=(%2) $P$G"

    echo Activated environment: %2
    set NOW_ENV=%2
    exit /b 0
)

@IF [%1] == [deactivate] (
    if NOT DEFINED NOW_ENV (
        echo ERROR: No environment activated.
        exit /b 1
    )
    echo Deactivated environment: %NOW_ENV%
    set NOW_ENV=
    @set "PROMPT=$P$G"
    exit /b 0
)
%SCRIPT_PATH% %*