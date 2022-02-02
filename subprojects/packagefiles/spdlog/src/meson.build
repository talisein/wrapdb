src = [
    'spdlog.cpp',
    'stdout_sinks.cpp',
    'color_sinks.cpp',
    'file_sinks.cpp',
    'async.cpp',
    'cfg.cpp'
]

if not get_option('external_fmt')
    src += 'fmt.cpp'
endif

spdlog_lib = library('spdlog', src,
    include_directories: inc,
    dependencies: spdlog_dependencies,
    cpp_args: spdlog_compile_args,
)
