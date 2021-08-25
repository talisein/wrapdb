if host_machine.system() == 'windows'
  conf.set('_WIN32_WINNT', '0x0502', description: 'Windows Server 2003 APIs')
  conf.set('NTDDI_VERSION', '0x05020000', description: 'Windows Server 2003 APIs')
  conf.set('WINVER', '0x0502', description: 'Windows Server 2003 APIs')
endif

foreach header: [
  'acl/libacl.h',
  'attr/xattr.h',
  'copyfile.h',
  'ctype.h',
  'errno.h',
  'ext2fs/ext2_fs.h',
  'fcntl.h',
  'grp.h',
  'inttypes.h',
  'langinfo.h',
  'limits.h',
  'linux/fiemap.h',
  'linux/fs.h',
  'linux/magic.h',
  'linux/types.h',
  'locale.h',
  'membership.h',
  'paths.h',
  'poll.h',
  'pthread.h',
  'pwd.h',
  'readpassphrase.h',
  'signal.h',
  'spawn.h',
  'stdarg.h',
  'stdint.h',
  'stdlib.h',
  'string.h',
  'sys/acl.h',
  'sys/cdefs.h',
  'sys/ea.h',
  'sys/extattr.h',
  'sys/.h',
  'sys/ioctl.h',
  'sys/mkdev.h',
  'sys/mount.h',
  'sys/param.h',
  'sys/poll.h',
  'sys/richacl.h',
  'sys/select.h',
  'sys/statfs.h',
  'sys/statvfs.h',
  'sys/sysmacros.h',
  'sys/time.h',
  'sys/utime.h',
  'sys/utsname.h',
  'sys/vfs.h',
  'sys/wait', # CHECK_HEADER_SYS_WAIT
  'sys/xattr.h',
  'time.h',
  'unistd.h',
  'utime.h',
  'wchar.h',
  'wctype.h',
  'windows.h',
  'wincrypt.h',
  'winioctl.h',
  ]
  conf.set('HAVE_' + header.underscorify().to_upper(), cc.has_header(header))
endforeach

foreach header: [
  'dirent.h',
  'sys/ndir.h',
  'sys/dir.h',
  'ndir.h',
  ]
  if cc.has_header_symbol(header, 'DIR')
    conf.set('HAVE_' + header.underscorify().to_upper(), true)
    break
  endif
endforeach

foreach symbol, header: {
  # libacl
  'acl_t': 'sys/acl.h',
  'acl_entry_t': 'sys/acl.h',
  'acl_permset_t': 'sys/acl.h',
  'acl_tag_t': 'sys/acl.h',

  # solaris
  'aclent_t': 'sys/acl.h',
  }
  conf.set('HAVE_' + symbol.underscorify().to_upper(), cc.has_header_symbol(header, symbol))
endforeach
