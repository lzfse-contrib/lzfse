project('lzfse', 'c',
  version : '1.0.0',
  default_options : [
    'c_std=c99',
    'warning_level=2'
  ]
)

# Source files for the lzfse core library
lzfse_sources = files(
  'src/lzfse_decode.c',
  'src/lzfse_decode_base.c',
  'src/lzfse_encode.c',
  'src/lzfse_encode_base.c',
  'src/lzfse_fse.c',
  'src/lzvn_decode_base.c',
  'src/lzvn_encode_base.c'
)

# Include directories
lzfse_inc = include_directories('src')

# Build lzfse library (builds both static and shared by default, 
# or use static_library() / shared_library() if specific type is needed)
lzfse_lib = library('lzfse',
  lzfse_sources,
  include_directories : lzfse_inc,
  install : true
)

# Declare dependency so other targets or subprojects can use it easily
lzfse_dep = declare_dependency(
  link_with : lzfse_lib,
  include_directories : lzfse_inc
)

# Build the lzfse command-line executable tool
lzfse_cli = executable('lzfse',
  'src/lzfse_main.c',
  include_directories : lzfse_inc,
  link_with : lzfse_lib,
  install : true
)

# Install the public header file
install_headers('src/lzfse.h')

# Generate pkg-config file (lzfse.pc)
pkg = import('pkgconfig')
pkg.generate(lzfse_lib,
  name : 'lzfse',
  filebase : 'lzfse',
  description : 'LZFSE compression library and command line tool',
  url : 'https://github.com/lzfse/lzfse'
)

# Round-trip tests: encode then decode each source file and compare checksums
if not get_option('disable_tests')
  python3 = import('python').find_installation('python3', required : false)
  if python3.found()
    round_trip = files('tests/round_trip.py')
    test_inputs = [
      'src/lzfse.h',
      'src/lzfse_decode.c',
      'src/lzfse_decode_base.c',
      'src/lzfse_encode.c',
      'src/lzfse_encode_base.c',
      'src/lzfse_encode_tables.h',
      'src/lzfse_fse.c',
      'src/lzfse_fse.h',
      'src/lzfse_internal.h',
      'src/lzfse_main.c',
      'src/lzfse_tunables.h',
      'src/lzvn_decode_base.c',
      'src/lzvn_decode_base.h',
      'src/lzvn_encode_base.c',
      'src/lzvn_encode_base.h'
    ]

    foreach f : test_inputs
      test('roundtrip-@0@'.format(f.underscorify()), python3,
        args : [round_trip, lzfse_cli, meson.current_source_dir() / f])
    endforeach
  endif
endif
