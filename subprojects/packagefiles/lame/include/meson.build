headers = [
  'lame.h',
]

vs_def = files('lame.def')[0]

version_script_dep = declare_dependency()
if ['ld.bfd', 'ld.gold'].contains(cc.get_linker_id())
  gnu_sym = custom_target('libmp3lame.ver GNU version script',
    input: 'libmp3lame.sym',
    output: 'libmp3lame.ver',
    command: [find_program('libtool-versionscript.py'), '@INPUT@', '@OUTPUT@'],
  )
  version_script_dep = declare_dependency(
    link_args: '-Wl,--version-script=@0@'.format(gnu_sym.full_path()),
    # files with unknown extension are treated as header deps
    sources: gnu_sym,
  )
endif

install_headers(headers, subdir : 'lame/')
