#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : harfbuzz
Version  : 2.7.2
Release  : 6
URL      : file:///insilications/build/clearlinux/packages/harfbuzz/harfbuzz-2.7.2.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/harfbuzz/harfbuzz-2.7.2.tar.gz
Summary  : HarfBuzz text shaping library
Group    : Development/Tools
License  : BSD-2-Clause
Requires: harfbuzz-bin = %{version}-%{release}
Requires: harfbuzz-data = %{version}-%{release}
Requires: harfbuzz-lib = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-meson
BuildRequires : cairo-dev
BuildRequires : docbook-xml
BuildRequires : findutils
BuildRequires : freetype-dev
BuildRequires : freetype-dev32
BuildRequires : freetype-staticdev
BuildRequires : freetype-staticdev32
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glib-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : graphite-dev
BuildRequires : graphite-staticdev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkg-config
BuildRequires : pkgconfig(32fontconfig)
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(32gobject-2.0)
BuildRequires : pkgconfig(32icu-uc)
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
BuildRequires : python3-core
BuildRequires : util-linux
BuildRequires : util-linux-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This is HarfBuzz, a text shaping library.
For bug reports, mailing list, and other information please visit:

%package bin
Summary: bin components for the harfbuzz package.
Group: Binaries
Requires: harfbuzz-data = %{version}-%{release}

%description bin
bin components for the harfbuzz package.


%package data
Summary: data components for the harfbuzz package.
Group: Data

%description data
data components for the harfbuzz package.


%package dev
Summary: dev components for the harfbuzz package.
Group: Development
Requires: harfbuzz-lib = %{version}-%{release}
Requires: harfbuzz-bin = %{version}-%{release}
Requires: harfbuzz-data = %{version}-%{release}
Provides: harfbuzz-devel = %{version}-%{release}
Requires: harfbuzz = %{version}-%{release}

%description dev
dev components for the harfbuzz package.


%package dev32
Summary: dev32 components for the harfbuzz package.
Group: Default
Requires: harfbuzz-lib32 = %{version}-%{release}
Requires: harfbuzz-bin = %{version}-%{release}
Requires: harfbuzz-data = %{version}-%{release}
Requires: harfbuzz-dev = %{version}-%{release}

%description dev32
dev32 components for the harfbuzz package.


%package lib
Summary: lib components for the harfbuzz package.
Group: Libraries
Requires: harfbuzz-data = %{version}-%{release}

%description lib
lib components for the harfbuzz package.


%package lib32
Summary: lib32 components for the harfbuzz package.
Group: Default
Requires: harfbuzz-data = %{version}-%{release}

%description lib32
lib32 components for the harfbuzz package.


%package staticdev
Summary: staticdev components for the harfbuzz package.
Group: Default
Requires: harfbuzz-dev = %{version}-%{release}

%description staticdev
staticdev components for the harfbuzz package.


%prep
%setup -q -n harfbuzz
cd %{_builddir}/harfbuzz
pushd ..
cp -a harfbuzz build32
popd

%build
## build_prepend content
#find . -type f -name '*.build' -print -exec touch {} \;
## build_prepend end
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1599679078
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -fPIC $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -fPIC $PGO_GEN"
export FFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -fPIC $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -fPIC $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%define _lto_cflags 1
#%define _lto_cflags %{nil}
#
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=1
export CCACHE_DIRECT=1
export CCACHE_SLOPPINESS=pch_defines,locale,time_macros
# export CCACHE_DISABLE=1
## altflags_pgo end
##
%define _lto_cflags 1
##
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%autogen  --enable-shared --enable-static --with-icu=yes --with-glib --with-freetype --with-cairo --with-icu --enable-introspection --with-graphite2 --with-gobject
## make_prepend content
#find . -type f -name '*.build' -print -exec touch {} \;
## make_prepend end
make  %{?_smp_mflags}

VERBOSE=1 V=1 make -j16 check
make clean
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%autogen   --enable-shared --enable-static --with-icu=yes --with-glib --with-freetype --with-cairo --with-icu --enable-introspection --with-graphite2 --with-gobject
## make_prepend content
#find . -type f -name '*.build' -print -exec touch {} \;
## make_prepend end
make  %{?_smp_mflags}

pushd ../build32/
## build_prepend content
#find . -type f -name '*.build' -print -exec touch {} \;
## build_prepend end
export CFLAGS="-g -O2 -fuse-linker-plugin -pipe"
export CXXFLAGS="-g -O2 -fuse-linker-plugin -fvisibility-inlines-hidden -pipe"
export LDFLAGS="-g -O2 -fuse-linker-plugin -pipe"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%autogen   --enable-shared --disable-static --with-icu=yes --with-glib --with-freetype --with-icu --disable-introspection --disable-cairo --without-cairo --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
## make_prepend content
#find . -type f -name '*.build' -print -exec touch {} \;
## make_prepend end
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1599679078
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hb-ot-shape-closure
/usr/bin/hb-shape
/usr/bin/hb-subset
/usr/bin/hb-view

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/HarfBuzz-0.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/harfbuzz/hb-aat-layout.h
/usr/include/harfbuzz/hb-aat.h
/usr/include/harfbuzz/hb-blob.h
/usr/include/harfbuzz/hb-buffer.h
/usr/include/harfbuzz/hb-common.h
/usr/include/harfbuzz/hb-deprecated.h
/usr/include/harfbuzz/hb-draw.h
/usr/include/harfbuzz/hb-face.h
/usr/include/harfbuzz/hb-font.h
/usr/include/harfbuzz/hb-ft.h
/usr/include/harfbuzz/hb-glib.h
/usr/include/harfbuzz/hb-gobject-enums.h
/usr/include/harfbuzz/hb-gobject-structs.h
/usr/include/harfbuzz/hb-gobject.h
/usr/include/harfbuzz/hb-graphite2.h
/usr/include/harfbuzz/hb-icu.h
/usr/include/harfbuzz/hb-map.h
/usr/include/harfbuzz/hb-ot-color.h
/usr/include/harfbuzz/hb-ot-deprecated.h
/usr/include/harfbuzz/hb-ot-font.h
/usr/include/harfbuzz/hb-ot-layout.h
/usr/include/harfbuzz/hb-ot-math.h
/usr/include/harfbuzz/hb-ot-meta.h
/usr/include/harfbuzz/hb-ot-metrics.h
/usr/include/harfbuzz/hb-ot-name.h
/usr/include/harfbuzz/hb-ot-shape.h
/usr/include/harfbuzz/hb-ot-var.h
/usr/include/harfbuzz/hb-ot.h
/usr/include/harfbuzz/hb-set.h
/usr/include/harfbuzz/hb-shape-plan.h
/usr/include/harfbuzz/hb-shape.h
/usr/include/harfbuzz/hb-style.h
/usr/include/harfbuzz/hb-subset.h
/usr/include/harfbuzz/hb-unicode.h
/usr/include/harfbuzz/hb-version.h
/usr/include/harfbuzz/hb.h
/usr/lib64/cmake/harfbuzz/harfbuzz-config.cmake
/usr/lib64/libharfbuzz-gobject.so
/usr/lib64/libharfbuzz-icu.so
/usr/lib64/libharfbuzz-subset.so
/usr/lib64/libharfbuzz.so
/usr/lib64/pkgconfig/harfbuzz-gobject.pc
/usr/lib64/pkgconfig/harfbuzz-icu.pc
/usr/lib64/pkgconfig/harfbuzz-subset.pc
/usr/lib64/pkgconfig/harfbuzz.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/cmake/harfbuzz/harfbuzz-config.cmake
/usr/lib32/libharfbuzz-icu.so
/usr/lib32/libharfbuzz-subset.so
/usr/lib32/libharfbuzz.so
/usr/lib32/pkgconfig/32harfbuzz-icu.pc
/usr/lib32/pkgconfig/32harfbuzz-subset.pc
/usr/lib32/pkgconfig/32harfbuzz.pc
/usr/lib32/pkgconfig/harfbuzz-icu.pc
/usr/lib32/pkgconfig/harfbuzz-subset.pc
/usr/lib32/pkgconfig/harfbuzz.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libharfbuzz-gobject.so.0
/usr/lib64/libharfbuzz-gobject.so.0.20702.0
/usr/lib64/libharfbuzz-icu.so.0
/usr/lib64/libharfbuzz-icu.so.0.20702.0
/usr/lib64/libharfbuzz-subset.so.0
/usr/lib64/libharfbuzz-subset.so.0.20702.0
/usr/lib64/libharfbuzz.so.0
/usr/lib64/libharfbuzz.so.0.20702.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libharfbuzz-icu.so.0
/usr/lib32/libharfbuzz-icu.so.0.20702.0
/usr/lib32/libharfbuzz-subset.so.0
/usr/lib32/libharfbuzz-subset.so.0.20702.0
/usr/lib32/libharfbuzz.so.0
/usr/lib32/libharfbuzz.so.0.20702.0

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libharfbuzz-gobject.a
/usr/lib64/libharfbuzz-icu.a
/usr/lib64/libharfbuzz-subset.a
/usr/lib64/libharfbuzz.a
