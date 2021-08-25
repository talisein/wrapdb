project('libarchive', 'c', version: '3.5.3',
  default_options: [] # -Wall is default, later on add -Wextra only for debug, only in cmake???
)

conf = configuration_data()

cc = meson.get_compiler('c')
add_project_arguments(cc.get_supported_arguments(['-Wformat', '-Wformat-security']), language: 'c')

# compression dependencies
zlib = dependency('zlib', required: get_option('zlib'))
bzip = dependency('bzip2', required: get_option('bz2lib'))
conf.set('HAVE_LIBBZ2', bzip.found())
libb2 = dependency('libb2', required: get_option('libb2'))
lz4 = dependency('liblz4', required: get_option('lz4'))
zstd = dependency('libzstd', required: get_option('zstd'))
lzma = dependency('liblzma', required: get_option('lzma'))
lzo2 = dependency('lzo2', required: get_option('lzo2'))

# just dependencies
xml2 = dependency('libxml-2.0', required: get_option('xml2'))
if not xml2.found()
  # FIXME: save either or as xar_backend
  expat = dependency('expat', required: get_option('expat'))
else
  expat = dependency('', required: false) # unneeded fallback
endif

# there are too many choices!!!
regex_lib = get_option('posix-regex-lib')
regex_dep = dependency('', required: false)
regex_found = false
if regex_lib != 'none'
  if regex_lib in ['libc', 'auto']
    regex_found = cc.has_function('regcomp')
  endif
  if not regex_found and regex_lib in ['libregex', 'auto']
    regex_dep = cc.find_library('regex', has_header: 'regex.h', required: false)
    regex_found = cc.has_function('regcomp', dependencies: regex_dep)
  endif
  if not regex_found # regex_lib in ['libpcreposix', 'auto']
    regex_dep = dependency('libpcreposix')
    regex_found = true # or error
  endif
endif


# iconv is messy

iconv_const_test = '''
    #include <stdlib.h>
    #include <iconv.h>
    int main() {
        @0@ char *ccp;
        iconv_t cd = iconv_open("", "");
        iconv(cd, &ccp, (size_t *)0, (char **)0, (size_t *)0);
        iconv_close(cd);
        return 0;
    }
    '''

## hopefully in the libc
iconv = dependency('', required: false)
iconv_const = ''
if not get_option('iconv').disabled() and cc.has_function('iconv_open')
  if cc.compiles(iconv_const_test.format('const'))
    iconv_const = 'const'
  elif not cc.compiles(iconv_const_test.format(''))
    error('impossible condition: iconv found but neither const nor non-const checks successfully compile')
  endif
  conf.set('HAVE_ICONV', true)
  conf.set('ICONV_CONST', iconv_const)
else
  iconv = cc.find_library('iconv', has_headers: 'iconv.h', required: get_option('iconv'))
  if iconv.found()
    conf.set('HAVE_ICONV', true)
    conf.set('ICONV_CONST', 'const')
    if cc.compiles(iconv_const_test.format('const'), dependencies: iconv)
      iconv_const = 'const'
    elif not cc.compiles(iconv_const_test.format(''), dependencies: iconv)
      error('impossible condition: iconv found but neither const nor non-const checks successfully compile')
    endif
  endif
endif

# acl is messy too, because POSIX never finalized anything
acl_found = false
if not get_option('acl').disabled()
  libacl = cc.find_library('acl', has_headers: 'sys/acl.h', required: false)
  if libacl.found()
    acl_found = cc.has_function('acl_get_file', dependencies: libacl)
  endif

  have_acl = cc.has_function('acl')
  have_facl = cc.has_function('facl')
endif


progs = get_option('progs')
if progs.contains('all')
  progs = ['bsdtar', 'bsdcat', 'bsdcpio']
endif

# do OS probing
subdir('build')

configure_file(input: 'build/cmake/config.h.in', output: 'config.h', configuration: conf, format: 'cmake@')
