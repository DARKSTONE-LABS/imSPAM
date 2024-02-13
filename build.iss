[Setup]
AppName=imSPAM
AppVersion=1.0
DefaultDirName={pf}\imSPAM
DefaultGroupName=imSPAM
OutputDir=E:\test\Output
OutputBaseFilename=imSPAM_setup
Compression=lzma
SolidCompression=yes
SetupIconFile=E:\test\imSPAM.ico

[Files]
Source: "E:\test\dist\imSPAM.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\imSPAM"; Filename: "{app}\imSPAM.exe"
Name: "{commondesktop}\imSPAM"; Filename: "{app}\imSPAM.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"

[Registry]
Root: HKCU; Subkey: "Software\imSPAM"; ValueType: string; ValueName: "Installed"; ValueData: "YES"; Flags: createvalueifdoesntexist

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
