# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Zahlenraten_1_0_2.py'],
             pathex=['C:\\Users\\berno\\Desktop\\Projekte\\Zahlenraten\\Zahlenraten_v1.0.2\\Zahlenraten_v1.0.2.j'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Zahlenraten_1_0_2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Zahlenraten_1_0_2')
