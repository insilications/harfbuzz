#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : harfbuzz
Version  : 2.6.7
Release  : 101
URL      : https://www.freedesktop.org/software/harfbuzz/release/harfbuzz-2.6.7.tar.xz
Source0  : https://www.freedesktop.org/software/harfbuzz/release/harfbuzz-2.6.7.tar.xz
Summary  : HarfBuzz text shaping library
Group    : Development/Tools
License  : BSD-2-Clause
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gcc-dev
BuildRequires : glib-dev
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : graphite-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkg-config
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-ft)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gmodule-export-2.0)
BuildRequires : pkgconfig(gmodule-no-export-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(icu-uc)
BuildRequires : util-linux
BuildRequires : util-linux-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This is HarfBuzz, a text shaping library.

%prep
%setup -q -n harfbuzz-2.6.7
cd %{_builddir}/harfbuzz-2.6.7

%build
## build_prepend content
find . -type f -name '*.json' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name '*.ninja' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
## build_prepend end
unset http_proxy
unset https_proxy
unset no_proxy
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595099132
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe $PGO_GEN"
export FFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-common -Wno-error -Wp,-D_REENTRANT
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#export CCACHE_DISABLE=1
## altflags_pgo end
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddefault_library=both -Dglib=enabled -Dgobject=enabled -Dcairo=enabled -Dfontconfig=enabled -Dicu=enabled -Dgraphite=enabled -Dfreetype=enabled -Dtests=enabled -Dintrospection=enabled  builddir
## make_prepend content
find . -type f -name '*.json' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name '*.ninja' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
## make_prepend end
ninja -v -C builddir

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
ninja -v -C builddir test

%install
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)
