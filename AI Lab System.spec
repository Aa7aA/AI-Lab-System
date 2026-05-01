[Setup]
AppId=AILABSYSTEM
AppName=AI Lab System
AppVersion=1.0.12
AppPublisher=AI Lab System
DefaultDirName={autopf}\AI Lab System
DefaultGroupName=AI Lab System
UninstallDisplayIcon={app}\AI Lab System.exe
OutputDir=output
OutputBaseFilename=AI-Lab-System-Setup-1.0.12
Compression=lzma
SolidCompression=yes
WizardStyle=modern
ArchitecturesInstallIn64BitMode=x64
PrivilegesRequired=admin
DisableProgramGroupPage=yes
CloseApplications=yes
RestartApplications=yes
AppMutex=AILabSystemMutex

[Files]
Source: "dist\AI Lab System\AI Lab System.exe"; DestDir: "{app}"; Flags: ignoreversion restartreplace
Source: "dist\AI Lab System\update_helper.exe"; DestDir: "{app}"; Flags: ignoreversion restartreplace
Source: "dist\AI Lab System\_internal\*"; DestDir: "{app}\_internal"; Flags: ignoreversion recursesubdirs createallsubdirs restartreplace

[Icons]
Name: "{autoprograms}\AI Lab System"; Filename: "{app}\AI Lab System.exe"
Name: "{autodesktop}\AI Lab System"; Filename: "{app}\AI Lab System.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; Flags: unchecked

[Run]
Filename: "{app}\AI Lab System.exe"; Description: "Launch AI Lab System"; Flags: nowait postinstall