@echo off
if "%~1"=="" (
  echo Kullanım: %~nx0 input_file output_file
  pause
  exit /b
)

if not exist "%~1" (
  echo Giriş dosyası bulunamadı: %~1
  pause
  exit /b
)

if "%~x2"=="" (
  echo Çıkış dosyası uzantısı belirtmelisiniz: %~nx0 input_file output_file
  pause
  exit /b
)

set valid_extensions=".bat" ".cmd"
set file_ext="%~x1"
set valid=false
for %%e in (%valid_extensions%) do (
  if /i %file_ext% equ %%e set valid=true
)
if not %valid%==true (
  echo Geçersiz dosya uzantısı: %~1
  echo Desteklenen uzantılar: %valid_extensions%
  pause
  exit /b
)

for /f %%i in ("certutil.exe") do if not exist "%%~$path:i" (
  echo CertUtil.exe bulunamadı.
  pause
  exit /b
)

>"temp.~b64" echo(//4mY2xzDQo=

certutil.exe -f -decode "temp.~b64" "%~n2%~x1" > nul
del "temp.~b64"
