#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : harfbuzz
Version  : 2.6.1
Release  : 93
URL      : https://www.freedesktop.org/software/harfbuzz/release/harfbuzz-2.6.1.tar.xz
Source0  : https://www.freedesktop.org/software/harfbuzz/release/harfbuzz-2.6.1.tar.xz
Summary  : OpenType text shaping engine
Group    : Development/Tools
License  : Apache-2.0 MIT OFL-1.1
Requires: harfbuzz-bin = %{version}-%{release}
Requires: harfbuzz-lib = %{version}-%{release}
Requires: harfbuzz-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : docbook-xml
BuildRequires : freetype-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : graphite-dev
BuildRequires : graphite-dev32
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkg-config
BuildRequires : pkgconfig(32cairo)
BuildRequires : pkgconfig(32cairo-ft)
BuildRequires : pkgconfig(32fontconfig)
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(32gobject-2.0)
BuildRequires : pkgconfig(32icu-uc)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-ft)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(icu-uc)

%description
This is HarfBuzz, a text shaping library.

%package bin
Summary: bin components for the harfbuzz package.
Group: Binaries
Requires: harfbuzz-license = %{version}-%{release}

%description bin
bin components for the harfbuzz package.


%package dev
Summary: dev components for the harfbuzz package.
Group: Development
Requires: harfbuzz-lib = %{version}-%{release}
Requires: harfbuzz-bin = %{version}-%{release}
Provides: harfbuzz-devel = %{version}-%{release}
Requires: harfbuzz = %{version}-%{release}
Requires: harfbuzz = %{version}-%{release}

%description dev
dev components for the harfbuzz package.


%package dev32
Summary: dev32 components for the harfbuzz package.
Group: Default
Requires: harfbuzz-lib32 = %{version}-%{release}
Requires: harfbuzz-bin = %{version}-%{release}
Requires: harfbuzz-dev = %{version}-%{release}

%description dev32
dev32 components for the harfbuzz package.


%package doc
Summary: doc components for the harfbuzz package.
Group: Documentation

%description doc
doc components for the harfbuzz package.


%package lib
Summary: lib components for the harfbuzz package.
Group: Libraries
Requires: harfbuzz-license = %{version}-%{release}

%description lib
lib components for the harfbuzz package.


%package lib32
Summary: lib32 components for the harfbuzz package.
Group: Default
Requires: harfbuzz-license = %{version}-%{release}

%description lib32
lib32 components for the harfbuzz package.


%package license
Summary: license components for the harfbuzz package.
Group: Default

%description license
license components for the harfbuzz package.


%prep
%setup -q -n harfbuzz-2.6.1
pushd ..
cp -a harfbuzz-2.6.1 build32
popd
pushd ..
cp -a harfbuzz-2.6.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1566661715
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --with-icu=yes --with-glib --with-freetype --with-cairo --with-icu --enable-introspection --with-graphite2
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32"
%configure --disable-static --with-icu=yes --with-glib --with-freetype --with-cairo --with-icu --enable-introspection --with-graphite2   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static --with-icu=yes --with-glib --with-freetype --with-cairo --with-icu --enable-introspection --with-graphite2
make  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1566661715
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/harfbuzz
cp COPYING %{buildroot}/usr/share/package-licenses/harfbuzz/COPYING
cp test/shaping/data/aots/COPYING %{buildroot}/usr/share/package-licenses/harfbuzz/test_shaping_data_aots_COPYING
cp test/shaping/data/in-house/COPYING %{buildroot}/usr/share/package-licenses/harfbuzz/test_shaping_data_in-house_COPYING
cp test/shaping/data/text-rendering-tests/COPYING %{buildroot}/usr/share/package-licenses/harfbuzz/test_shaping_data_text-rendering-tests_COPYING
cp test/shaping/texts/in-house/shaper-indic/script-assamese/utrrs/LICENSE %{buildroot}/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-assamese_utrrs_LICENSE
cp test/shaping/texts/in-house/shaper-indic/script-bengali/utrrs/LICENSE %{buildroot}/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-bengali_utrrs_LICENSE
cp test/shaping/texts/in-house/shaper-indic/script-devanagari/utrrs/LICENSE %{buildroot}/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-devanagari_utrrs_LICENSE
cp test/shaping/texts/in-house/shaper-indic/script-gujarati/utrrs/LICENSE %{buildroot}/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-gujarati_utrrs_LICENSE
cp test/shaping/texts/in-house/shaper-indic/script-gurmukhi/utrrs/LICENSE %{buildroot}/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-gurmukhi_utrrs_LICENSE
cp test/shaping/texts/in-house/shaper-indic/script-kannada/utrrs/LICENSE %{buildroot}/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-kannada_utrrs_LICENSE
cp test/shaping/texts/in-house/shaper-indic/script-malayalam/utrrs/LICENSE %{buildroot}/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-malayalam_utrrs_LICENSE
cp test/shaping/texts/in-house/shaper-indic/script-oriya/utrrs/LICENSE %{buildroot}/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-oriya_utrrs_LICENSE
cp test/shaping/texts/in-house/shaper-indic/script-sinhala/utrrs/LICENSE %{buildroot}/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-sinhala_utrrs_LICENSE
cp test/shaping/texts/in-house/shaper-indic/script-tamil/utrrs/LICENSE %{buildroot}/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-tamil_utrrs_LICENSE
cp test/shaping/texts/in-house/shaper-indic/script-telugu/utrrs/LICENSE %{buildroot}/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-telugu_utrrs_LICENSE
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_avx2
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/haswell/hb-ot-shape-closure
/usr/bin/haswell/hb-shape
/usr/bin/haswell/hb-subset
/usr/bin/haswell/hb-view
/usr/bin/hb-ot-shape-closure
/usr/bin/hb-shape
/usr/bin/hb-subset
/usr/bin/hb-view

%files dev
%defattr(-,root,root,-)
/usr/include/harfbuzz/hb-aat-layout.h
/usr/include/harfbuzz/hb-aat.h
/usr/include/harfbuzz/hb-blob.h
/usr/include/harfbuzz/hb-buffer.h
/usr/include/harfbuzz/hb-common.h
/usr/include/harfbuzz/hb-deprecated.h
/usr/include/harfbuzz/hb-face.h
/usr/include/harfbuzz/hb-font.h
/usr/include/harfbuzz/hb-ft.h
/usr/include/harfbuzz/hb-glib.h
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
/usr/include/harfbuzz/hb-subset.h
/usr/include/harfbuzz/hb-unicode.h
/usr/include/harfbuzz/hb-version.h
/usr/include/harfbuzz/hb.h
/usr/lib64/cmake/harfbuzz/harfbuzz-config.cmake
/usr/lib64/haswell/libharfbuzz-subset.so
/usr/lib64/haswell/libharfbuzz.so
/usr/lib64/libharfbuzz-icu.so
/usr/lib64/libharfbuzz-subset.so
/usr/lib64/libharfbuzz.so
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

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/harfbuzz/HarfBuzz.png
/usr/share/gtk-doc/html/harfbuzz/HarfBuzz.svg
/usr/share/gtk-doc/html/harfbuzz/a-clustering-example-for-levels-0-and-1.html
/usr/share/gtk-doc/html/harfbuzz/aat-shaping.html
/usr/share/gtk-doc/html/harfbuzz/adding-text-to-the-buffer.html
/usr/share/gtk-doc/html/harfbuzz/annotation-glossary.html
/usr/share/gtk-doc/html/harfbuzz/api-index-full.html
/usr/share/gtk-doc/html/harfbuzz/buffers-language-script-and-direction.html
/usr/share/gtk-doc/html/harfbuzz/building.html
/usr/share/gtk-doc/html/harfbuzz/ch01s03.html
/usr/share/gtk-doc/html/harfbuzz/ch03s02.html
/usr/share/gtk-doc/html/harfbuzz/ch03s03.html
/usr/share/gtk-doc/html/harfbuzz/ch11.html
/usr/share/gtk-doc/html/harfbuzz/ch12.html
/usr/share/gtk-doc/html/harfbuzz/ch13.html
/usr/share/gtk-doc/html/harfbuzz/ch14.html
/usr/share/gtk-doc/html/harfbuzz/clusters.html
/usr/share/gtk-doc/html/harfbuzz/complex-scripts.html
/usr/share/gtk-doc/html/harfbuzz/customizing-unicode-functions.html
/usr/share/gtk-doc/html/harfbuzz/fonts-and-faces-custom-functions.html
/usr/share/gtk-doc/html/harfbuzz/fonts-and-faces-native-opentype.html
/usr/share/gtk-doc/html/harfbuzz/fonts-and-faces-variable.html
/usr/share/gtk-doc/html/harfbuzz/fonts-and-faces.html
/usr/share/gtk-doc/html/harfbuzz/getting-started.html
/usr/share/gtk-doc/html/harfbuzz/graphite-shaping.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-aat-layout.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-blob.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-buffer.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-common.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-coretext.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-deprecated.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-face.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-font.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ft.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-glib.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-gobject.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-graphite2.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-icu.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-map.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-color.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-font.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-layout.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-math.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-name.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-shape.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-var.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-set.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-shape-plan.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-shape.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-unicode.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-uniscribe.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-version.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz.devhelp2
/usr/share/gtk-doc/html/harfbuzz/home.png
/usr/share/gtk-doc/html/harfbuzz/index.html
/usr/share/gtk-doc/html/harfbuzz/install-harfbuzz.html
/usr/share/gtk-doc/html/harfbuzz/left-insensitive.png
/usr/share/gtk-doc/html/harfbuzz/left.png
/usr/share/gtk-doc/html/harfbuzz/level-2.html
/usr/share/gtk-doc/html/harfbuzz/object-model-blobs.html
/usr/share/gtk-doc/html/harfbuzz/object-model-lifecycle.html
/usr/share/gtk-doc/html/harfbuzz/object-model-object-types.html
/usr/share/gtk-doc/html/harfbuzz/object-model-user-data.html
/usr/share/gtk-doc/html/harfbuzz/object-model.html
/usr/share/gtk-doc/html/harfbuzz/opentype-shaping-models.html
/usr/share/gtk-doc/html/harfbuzz/pt01.html
/usr/share/gtk-doc/html/harfbuzz/pt02.html
/usr/share/gtk-doc/html/harfbuzz/reordering-in-levels-0-and-1.html
/usr/share/gtk-doc/html/harfbuzz/right-insensitive.png
/usr/share/gtk-doc/html/harfbuzz/right.png
/usr/share/gtk-doc/html/harfbuzz/setting-buffer-properties.html
/usr/share/gtk-doc/html/harfbuzz/shaping-and-shape-plans.html
/usr/share/gtk-doc/html/harfbuzz/shaping-concepts.html
/usr/share/gtk-doc/html/harfbuzz/shaping-opentype-features.html
/usr/share/gtk-doc/html/harfbuzz/shaping-operations.html
/usr/share/gtk-doc/html/harfbuzz/shaping-plans-and-caching.html
/usr/share/gtk-doc/html/harfbuzz/shaping-shaper-selection.html
/usr/share/gtk-doc/html/harfbuzz/style.css
/usr/share/gtk-doc/html/harfbuzz/text-runs.html
/usr/share/gtk-doc/html/harfbuzz/the-distinction-between-levels-0-and-1.html
/usr/share/gtk-doc/html/harfbuzz/unicode-character-categories.html
/usr/share/gtk-doc/html/harfbuzz/up-insensitive.png
/usr/share/gtk-doc/html/harfbuzz/up.png
/usr/share/gtk-doc/html/harfbuzz/utilities-common-types-apis.html
/usr/share/gtk-doc/html/harfbuzz/utilities-ucdn.html
/usr/share/gtk-doc/html/harfbuzz/utilities.html
/usr/share/gtk-doc/html/harfbuzz/what-harfbuzz-doesnt-do.html
/usr/share/gtk-doc/html/harfbuzz/what-is-harfbuzz.html
/usr/share/gtk-doc/html/harfbuzz/why-do-i-need-a-shaping-engine.html
/usr/share/gtk-doc/html/harfbuzz/why-is-it-called-harfbuzz.html
/usr/share/gtk-doc/html/harfbuzz/working-with-harfbuzz-clusters.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libharfbuzz-subset.so.0
/usr/lib64/haswell/libharfbuzz-subset.so.0.20600.1
/usr/lib64/haswell/libharfbuzz.so.0
/usr/lib64/haswell/libharfbuzz.so.0.20600.1
/usr/lib64/libharfbuzz-icu.so.0
/usr/lib64/libharfbuzz-icu.so.0.20600.1
/usr/lib64/libharfbuzz-subset.so.0
/usr/lib64/libharfbuzz-subset.so.0.20600.1
/usr/lib64/libharfbuzz.so.0
/usr/lib64/libharfbuzz.so.0.20600.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libharfbuzz-icu.so.0
/usr/lib32/libharfbuzz-icu.so.0.20600.1
/usr/lib32/libharfbuzz-subset.so.0
/usr/lib32/libharfbuzz-subset.so.0.20600.1
/usr/lib32/libharfbuzz.so.0
/usr/lib32/libharfbuzz.so.0.20600.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/harfbuzz/COPYING
/usr/share/package-licenses/harfbuzz/test_shaping_data_aots_COPYING
/usr/share/package-licenses/harfbuzz/test_shaping_data_in-house_COPYING
/usr/share/package-licenses/harfbuzz/test_shaping_data_text-rendering-tests_COPYING
/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-assamese_utrrs_LICENSE
/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-bengali_utrrs_LICENSE
/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-devanagari_utrrs_LICENSE
/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-gujarati_utrrs_LICENSE
/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-gurmukhi_utrrs_LICENSE
/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-kannada_utrrs_LICENSE
/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-malayalam_utrrs_LICENSE
/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-oriya_utrrs_LICENSE
/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-sinhala_utrrs_LICENSE
/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-tamil_utrrs_LICENSE
/usr/share/package-licenses/harfbuzz/test_shaping_texts_in-house_shaper-indic_script-telugu_utrrs_LICENSE
