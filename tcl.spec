%define keepstatic 1
Name     : tcl
Version  : 8.6.5
Release  : 29
URL      : http://downloads.sourceforge.net/tcl/tcl8.6.5-src.tar.gz
Source0  : http://downloads.sourceforge.net/tcl/tcl8.6.5-src.tar.gz
Summary  : Tcl scripting language development environment
Group    : Development/Tools
License  : TCL
Requires: tcl-bin
Requires: tcl-lib
Requires: tcl-doc
Requires: tcl-data
BuildRequires : cmake
BuildRequires : procps-ng
BuildRequires : tzdata
BuildRequires : zlib-dev
BuildRequires : sqlite-autoconf-dev
Patch1: build.patch

%description
The Tcl (Tool Command Language) provides a powerful platform for
creating integration applications that tie together diverse
applications, protocols, devices, and frameworks.  When paired with
the Tk toolkit, Tcl provides the fastest and most powerful way to
create GUI applications that run on PCs, Unix, and Mac OS X.  Tcl
can also be used for a variety of web-related tasks and for creating
powerful command languages for applications.

%package bin
Summary: bin components for the tcl package.
Group: Binaries
Requires: tcl-data

%description bin
bin components for the tcl package.


%package data
Summary: data components for the tcl package.
Group: Data

%description data
data components for the tcl package.


%package dev
Summary: dev components for the tcl package.
Group: Development
Requires: tcl-lib
Requires: tcl-bin
Requires: tcl-data
Provides: tcl-devel

%description dev
dev components for the tcl package.


%package doc
Summary: doc components for the tcl package.
Group: Documentation

%description doc
doc components for the tcl package.


%package lib
Summary: lib components for the tcl package.
Group: Libraries
Requires: tcl-data

%description lib
lib components for the tcl package.


%prep
%setup -q -n tcl8.6.5
%patch1 -p1

%build
pushd unix/
export CFLAGS="$CFLAGS -O3"
%configure  --enable-symbols

# build binary without funroll-loops
make V=1  %{?_smp_mflags}
popd

%install
rm -rf %{buildroot}
pushd unix/
%make_install install-private-headers
popd

# build binary with funroll-loops
export CFLAGS="$CFLAGS -O3 -ffunction-sections -fno-semantic-interposition
-fopt-info-vec -flto"
export CXXFLAGS="$CXXFLAGS -O3 -ffunction-sections -fno-semantic-interposition
-fopt-info-vec"
pushd unix/
make V=1  %{?_smp_mflags}
%make_install install-binaries
popd
## make_install_append content
ln -s /usr/bin/tclsh8.6 %{buildroot}/usr/bin/tclsh


%files
%defattr(-,root,root,-)
/usr/lib/tcl8.6/auto.tcl
/usr/lib/tcl8.6/clock.tcl
/usr/lib/tcl8.6/encoding/ascii.enc
/usr/lib/tcl8.6/encoding/big5.enc
/usr/lib/tcl8.6/encoding/cp1250.enc
/usr/lib/tcl8.6/encoding/cp1251.enc
/usr/lib/tcl8.6/encoding/cp1252.enc
/usr/lib/tcl8.6/encoding/cp1253.enc
/usr/lib/tcl8.6/encoding/cp1254.enc
/usr/lib/tcl8.6/encoding/cp1255.enc
/usr/lib/tcl8.6/encoding/cp1256.enc
/usr/lib/tcl8.6/encoding/cp1257.enc
/usr/lib/tcl8.6/encoding/cp1258.enc
/usr/lib/tcl8.6/encoding/cp437.enc
/usr/lib/tcl8.6/encoding/cp737.enc
/usr/lib/tcl8.6/encoding/cp775.enc
/usr/lib/tcl8.6/encoding/cp850.enc
/usr/lib/tcl8.6/encoding/cp852.enc
/usr/lib/tcl8.6/encoding/cp855.enc
/usr/lib/tcl8.6/encoding/cp857.enc
/usr/lib/tcl8.6/encoding/cp860.enc
/usr/lib/tcl8.6/encoding/cp861.enc
/usr/lib/tcl8.6/encoding/cp862.enc
/usr/lib/tcl8.6/encoding/cp863.enc
/usr/lib/tcl8.6/encoding/cp864.enc
/usr/lib/tcl8.6/encoding/cp865.enc
/usr/lib/tcl8.6/encoding/cp866.enc
/usr/lib/tcl8.6/encoding/cp869.enc
/usr/lib/tcl8.6/encoding/cp874.enc
/usr/lib/tcl8.6/encoding/cp932.enc
/usr/lib/tcl8.6/encoding/cp936.enc
/usr/lib/tcl8.6/encoding/cp949.enc
/usr/lib/tcl8.6/encoding/cp950.enc
/usr/lib/tcl8.6/encoding/dingbats.enc
/usr/lib/tcl8.6/encoding/ebcdic.enc
/usr/lib/tcl8.6/encoding/euc-cn.enc
/usr/lib/tcl8.6/encoding/euc-jp.enc
/usr/lib/tcl8.6/encoding/euc-kr.enc
/usr/lib/tcl8.6/encoding/gb12345.enc
/usr/lib/tcl8.6/encoding/gb1988.enc
/usr/lib/tcl8.6/encoding/gb2312-raw.enc
/usr/lib/tcl8.6/encoding/gb2312.enc
/usr/lib/tcl8.6/encoding/iso2022-jp.enc
/usr/lib/tcl8.6/encoding/iso2022-kr.enc
/usr/lib/tcl8.6/encoding/iso2022.enc
/usr/lib/tcl8.6/encoding/iso8859-1.enc
/usr/lib/tcl8.6/encoding/iso8859-10.enc
/usr/lib/tcl8.6/encoding/iso8859-13.enc
/usr/lib/tcl8.6/encoding/iso8859-14.enc
/usr/lib/tcl8.6/encoding/iso8859-15.enc
/usr/lib/tcl8.6/encoding/iso8859-16.enc
/usr/lib/tcl8.6/encoding/iso8859-2.enc
/usr/lib/tcl8.6/encoding/iso8859-3.enc
/usr/lib/tcl8.6/encoding/iso8859-4.enc
/usr/lib/tcl8.6/encoding/iso8859-5.enc
/usr/lib/tcl8.6/encoding/iso8859-6.enc
/usr/lib/tcl8.6/encoding/iso8859-7.enc
/usr/lib/tcl8.6/encoding/iso8859-8.enc
/usr/lib/tcl8.6/encoding/iso8859-9.enc
/usr/lib/tcl8.6/encoding/jis0201.enc
/usr/lib/tcl8.6/encoding/jis0208.enc
/usr/lib/tcl8.6/encoding/jis0212.enc
/usr/lib/tcl8.6/encoding/koi8-r.enc
/usr/lib/tcl8.6/encoding/koi8-u.enc
/usr/lib/tcl8.6/encoding/ksc5601.enc
/usr/lib/tcl8.6/encoding/macCentEuro.enc
/usr/lib/tcl8.6/encoding/macCroatian.enc
/usr/lib/tcl8.6/encoding/macCyrillic.enc
/usr/lib/tcl8.6/encoding/macDingbats.enc
/usr/lib/tcl8.6/encoding/macGreek.enc
/usr/lib/tcl8.6/encoding/macIceland.enc
/usr/lib/tcl8.6/encoding/macJapan.enc
/usr/lib/tcl8.6/encoding/macRoman.enc
/usr/lib/tcl8.6/encoding/macRomania.enc
/usr/lib/tcl8.6/encoding/macThai.enc
/usr/lib/tcl8.6/encoding/macTurkish.enc
/usr/lib/tcl8.6/encoding/macUkraine.enc
/usr/lib/tcl8.6/encoding/shiftjis.enc
/usr/lib/tcl8.6/encoding/symbol.enc
/usr/lib/tcl8.6/encoding/tis-620.enc
/usr/lib/tcl8.6/history.tcl
/usr/lib/tcl8.6/http1.0/http.tcl
/usr/lib/tcl8.6/http1.0/pkgIndex.tcl
/usr/lib/tcl8.6/init.tcl
/usr/lib/tcl8.6/msgs/af.msg
/usr/lib/tcl8.6/msgs/af_za.msg
/usr/lib/tcl8.6/msgs/ar.msg
/usr/lib/tcl8.6/msgs/ar_in.msg
/usr/lib/tcl8.6/msgs/ar_jo.msg
/usr/lib/tcl8.6/msgs/ar_lb.msg
/usr/lib/tcl8.6/msgs/ar_sy.msg
/usr/lib/tcl8.6/msgs/be.msg
/usr/lib/tcl8.6/msgs/bg.msg
/usr/lib/tcl8.6/msgs/bn.msg
/usr/lib/tcl8.6/msgs/bn_in.msg
/usr/lib/tcl8.6/msgs/ca.msg
/usr/lib/tcl8.6/msgs/cs.msg
/usr/lib/tcl8.6/msgs/da.msg
/usr/lib/tcl8.6/msgs/de.msg
/usr/lib/tcl8.6/msgs/de_at.msg
/usr/lib/tcl8.6/msgs/de_be.msg
/usr/lib/tcl8.6/msgs/el.msg
/usr/lib/tcl8.6/msgs/en_au.msg
/usr/lib/tcl8.6/msgs/en_be.msg
/usr/lib/tcl8.6/msgs/en_bw.msg
/usr/lib/tcl8.6/msgs/en_ca.msg
/usr/lib/tcl8.6/msgs/en_gb.msg
/usr/lib/tcl8.6/msgs/en_hk.msg
/usr/lib/tcl8.6/msgs/en_ie.msg
/usr/lib/tcl8.6/msgs/en_in.msg
/usr/lib/tcl8.6/msgs/en_nz.msg
/usr/lib/tcl8.6/msgs/en_ph.msg
/usr/lib/tcl8.6/msgs/en_sg.msg
/usr/lib/tcl8.6/msgs/en_za.msg
/usr/lib/tcl8.6/msgs/en_zw.msg
/usr/lib/tcl8.6/msgs/eo.msg
/usr/lib/tcl8.6/msgs/es.msg
/usr/lib/tcl8.6/msgs/es_ar.msg
/usr/lib/tcl8.6/msgs/es_bo.msg
/usr/lib/tcl8.6/msgs/es_cl.msg
/usr/lib/tcl8.6/msgs/es_co.msg
/usr/lib/tcl8.6/msgs/es_cr.msg
/usr/lib/tcl8.6/msgs/es_do.msg
/usr/lib/tcl8.6/msgs/es_ec.msg
/usr/lib/tcl8.6/msgs/es_gt.msg
/usr/lib/tcl8.6/msgs/es_hn.msg
/usr/lib/tcl8.6/msgs/es_mx.msg
/usr/lib/tcl8.6/msgs/es_ni.msg
/usr/lib/tcl8.6/msgs/es_pa.msg
/usr/lib/tcl8.6/msgs/es_pe.msg
/usr/lib/tcl8.6/msgs/es_pr.msg
/usr/lib/tcl8.6/msgs/es_py.msg
/usr/lib/tcl8.6/msgs/es_sv.msg
/usr/lib/tcl8.6/msgs/es_uy.msg
/usr/lib/tcl8.6/msgs/es_ve.msg
/usr/lib/tcl8.6/msgs/et.msg
/usr/lib/tcl8.6/msgs/eu.msg
/usr/lib/tcl8.6/msgs/eu_es.msg
/usr/lib/tcl8.6/msgs/fa.msg
/usr/lib/tcl8.6/msgs/fa_in.msg
/usr/lib/tcl8.6/msgs/fa_ir.msg
/usr/lib/tcl8.6/msgs/fi.msg
/usr/lib/tcl8.6/msgs/fo.msg
/usr/lib/tcl8.6/msgs/fo_fo.msg
/usr/lib/tcl8.6/msgs/fr.msg
/usr/lib/tcl8.6/msgs/fr_be.msg
/usr/lib/tcl8.6/msgs/fr_ca.msg
/usr/lib/tcl8.6/msgs/fr_ch.msg
/usr/lib/tcl8.6/msgs/ga.msg
/usr/lib/tcl8.6/msgs/ga_ie.msg
/usr/lib/tcl8.6/msgs/gl.msg
/usr/lib/tcl8.6/msgs/gl_es.msg
/usr/lib/tcl8.6/msgs/gv.msg
/usr/lib/tcl8.6/msgs/gv_gb.msg
/usr/lib/tcl8.6/msgs/he.msg
/usr/lib/tcl8.6/msgs/hi.msg
/usr/lib/tcl8.6/msgs/hi_in.msg
/usr/lib/tcl8.6/msgs/hr.msg
/usr/lib/tcl8.6/msgs/hu.msg
/usr/lib/tcl8.6/msgs/id.msg
/usr/lib/tcl8.6/msgs/id_id.msg
/usr/lib/tcl8.6/msgs/is.msg
/usr/lib/tcl8.6/msgs/it.msg
/usr/lib/tcl8.6/msgs/it_ch.msg
/usr/lib/tcl8.6/msgs/ja.msg
/usr/lib/tcl8.6/msgs/kl.msg
/usr/lib/tcl8.6/msgs/kl_gl.msg
/usr/lib/tcl8.6/msgs/ko.msg
/usr/lib/tcl8.6/msgs/ko_kr.msg
/usr/lib/tcl8.6/msgs/kok.msg
/usr/lib/tcl8.6/msgs/kok_in.msg
/usr/lib/tcl8.6/msgs/kw.msg
/usr/lib/tcl8.6/msgs/kw_gb.msg
/usr/lib/tcl8.6/msgs/lt.msg
/usr/lib/tcl8.6/msgs/lv.msg
/usr/lib/tcl8.6/msgs/mk.msg
/usr/lib/tcl8.6/msgs/mr.msg
/usr/lib/tcl8.6/msgs/mr_in.msg
/usr/lib/tcl8.6/msgs/ms.msg
/usr/lib/tcl8.6/msgs/ms_my.msg
/usr/lib/tcl8.6/msgs/mt.msg
/usr/lib/tcl8.6/msgs/nb.msg
/usr/lib/tcl8.6/msgs/nl.msg
/usr/lib/tcl8.6/msgs/nl_be.msg
/usr/lib/tcl8.6/msgs/nn.msg
/usr/lib/tcl8.6/msgs/pl.msg
/usr/lib/tcl8.6/msgs/pt.msg
/usr/lib/tcl8.6/msgs/pt_br.msg
/usr/lib/tcl8.6/msgs/ro.msg
/usr/lib/tcl8.6/msgs/ru.msg
/usr/lib/tcl8.6/msgs/ru_ua.msg
/usr/lib/tcl8.6/msgs/sh.msg
/usr/lib/tcl8.6/msgs/sk.msg
/usr/lib/tcl8.6/msgs/sl.msg
/usr/lib/tcl8.6/msgs/sq.msg
/usr/lib/tcl8.6/msgs/sr.msg
/usr/lib/tcl8.6/msgs/sv.msg
/usr/lib/tcl8.6/msgs/sw.msg
/usr/lib/tcl8.6/msgs/ta.msg
/usr/lib/tcl8.6/msgs/ta_in.msg
/usr/lib/tcl8.6/msgs/te.msg
/usr/lib/tcl8.6/msgs/te_in.msg
/usr/lib/tcl8.6/msgs/th.msg
/usr/lib/tcl8.6/msgs/tr.msg
/usr/lib/tcl8.6/msgs/uk.msg
/usr/lib/tcl8.6/msgs/vi.msg
/usr/lib/tcl8.6/msgs/zh.msg
/usr/lib/tcl8.6/msgs/zh_cn.msg
/usr/lib/tcl8.6/msgs/zh_hk.msg
/usr/lib/tcl8.6/msgs/zh_sg.msg
/usr/lib/tcl8.6/msgs/zh_tw.msg
/usr/lib/tcl8.6/opt0.4/optparse.tcl
/usr/lib/tcl8.6/opt0.4/pkgIndex.tcl
/usr/lib/tcl8.6/package.tcl
/usr/lib/tcl8.6/parray.tcl
/usr/lib/tcl8.6/safe.tcl
/usr/lib/tcl8.6/tclAppInit.c
/usr/lib/tcl8.6/tclIndex
/usr/lib/tcl8.6/tm.tcl
/usr/lib/tcl8.6/word.tcl
/usr/lib/tcl8/8.4/platform-*.tm
/usr/lib/tcl8/8.4/platform/shell-*.tm
/usr/lib/tcl8/8.5/msgcat-*.tm
/usr/lib/tcl8/8.5/tcltest-*.tm
/usr/lib/tcl8/8.6/http-*.tm
/usr/lib64/itcl*/itcl.tcl
/usr/lib64/itcl*/itclConfig.sh
/usr/lib64/itcl*/itclHullCmds.tcl
/usr/lib64/itcl*/itclWidget.tcl
/usr/lib64/itcl*/libitclstub*.a
/usr/lib64/itcl*/pkgIndex.tcl
/usr/lib64/sqlite3*/pkgIndex.tcl
/usr/lib64/tcl8/8.6/tdbc/sqlite3-*.tm
/usr/lib64/tclConfig.sh
/usr/lib64/tclooConfig.sh
/usr/lib64/tdbc*/libtdbcstub*.a
/usr/lib64/tdbc*/pkgIndex.tcl
/usr/lib64/tdbc*/tdbc.tcl
/usr/lib64/tdbc*/tdbcConfig.sh
/usr/lib64/tdbcmysql*/pkgIndex.tcl
/usr/lib64/tdbcmysql*/tdbcmysql.tcl
/usr/lib64/tdbcodbc*/pkgIndex.tcl
/usr/lib64/tdbcodbc*/tdbcodbc.tcl
/usr/lib64/tdbcpostgres*/pkgIndex.tcl
/usr/lib64/tdbcpostgres*/tdbcpostgres.tcl
/usr/lib64/thread*/pkgIndex.tcl
/usr/lib64/thread*/ttrace.tcl

%files bin
%defattr(-,root,root,-)
/usr/bin/tclsh
/usr/bin/tclsh8.6
%exclude /usr/bin/sqlite3_analyzer

%files data
%defattr(-,root,root,-)
/usr/share/man/mann/Tcl.n
/usr/share/man/mann/after.n
/usr/share/man/mann/append.n
/usr/share/man/mann/apply.n
/usr/share/man/mann/argc.n
/usr/share/man/mann/argv.n
/usr/share/man/mann/argv0.n
/usr/share/man/mann/array.n
/usr/share/man/mann/auto_execok.n
/usr/share/man/mann/auto_import.n
/usr/share/man/mann/auto_load.n
/usr/share/man/mann/auto_mkindex.n
/usr/share/man/mann/auto_path.n
/usr/share/man/mann/auto_qualify.n
/usr/share/man/mann/auto_reset.n
/usr/share/man/mann/bgerror.n
/usr/share/man/mann/binary.n
/usr/share/man/mann/body.n
/usr/share/man/mann/break.n
/usr/share/man/mann/case.n
/usr/share/man/mann/catch.n
/usr/share/man/mann/cd.n
/usr/share/man/mann/chan.n
/usr/share/man/mann/class.n
/usr/share/man/mann/clock.n
/usr/share/man/mann/close.n
/usr/share/man/mann/code.n
/usr/share/man/mann/concat.n
/usr/share/man/mann/configbody.n
/usr/share/man/mann/continue.n
/usr/share/man/mann/coroutine.n
/usr/share/man/mann/dde.n
/usr/share/man/mann/delete.n
/usr/share/man/mann/dict.n
/usr/share/man/mann/encoding.n
/usr/share/man/mann/ensemble.n
/usr/share/man/mann/env.n
/usr/share/man/mann/eof.n
/usr/share/man/mann/error.n
/usr/share/man/mann/errorCode.n
/usr/share/man/mann/errorInfo.n
/usr/share/man/mann/eval.n
/usr/share/man/mann/exec.n
/usr/share/man/mann/exit.n
/usr/share/man/mann/expr.n
/usr/share/man/mann/fblocked.n
/usr/share/man/mann/fconfigure.n
/usr/share/man/mann/fcopy.n
/usr/share/man/mann/file.n
/usr/share/man/mann/fileevent.n
/usr/share/man/mann/filename.n
/usr/share/man/mann/find.n
/usr/share/man/mann/flush.n
/usr/share/man/mann/for.n
/usr/share/man/mann/foreach.n
/usr/share/man/mann/format.n
/usr/share/man/mann/gets.n
/usr/share/man/mann/glob.n
/usr/share/man/mann/global.n
/usr/share/man/mann/history.n
/usr/share/man/mann/http.n
/usr/share/man/mann/if.n
/usr/share/man/mann/incr.n
/usr/share/man/mann/info.n
/usr/share/man/mann/interp.n
/usr/share/man/mann/is.n
/usr/share/man/mann/itcl.n
/usr/share/man/mann/itclcomponent.n
/usr/share/man/mann/itcldelegate.n
/usr/share/man/mann/itclextendedclass.n
/usr/share/man/mann/itcloption.n
/usr/share/man/mann/itclvars.n
/usr/share/man/mann/itclwidget.n
/usr/share/man/mann/join.n
/usr/share/man/mann/lappend.n
/usr/share/man/mann/lassign.n
/usr/share/man/mann/lindex.n
/usr/share/man/mann/linsert.n
/usr/share/man/mann/list.n
/usr/share/man/mann/llength.n
/usr/share/man/mann/lmap.n
/usr/share/man/mann/load.n
/usr/share/man/mann/local.n
/usr/share/man/mann/lrange.n
/usr/share/man/mann/lrepeat.n
/usr/share/man/mann/lreplace.n
/usr/share/man/mann/lreverse.n
/usr/share/man/mann/lsearch.n
/usr/share/man/mann/lset.n
/usr/share/man/mann/lsort.n
/usr/share/man/mann/mathfunc.n
/usr/share/man/mann/mathop.n
/usr/share/man/mann/memory.n
/usr/share/man/mann/msgcat.n
/usr/share/man/mann/my.n
/usr/share/man/mann/namespace.n
/usr/share/man/mann/next.n
/usr/share/man/mann/nextto.n
/usr/share/man/mann/oo_class.n
/usr/share/man/mann/oo_copy.n
/usr/share/man/mann/oo_define.n
/usr/share/man/mann/oo_objdefine.n
/usr/share/man/mann/oo_object.n
/usr/share/man/mann/open.n
/usr/share/man/mann/package.n
/usr/share/man/mann/parray.n
/usr/share/man/mann/pid.n
/usr/share/man/mann/pkg_create.n
/usr/share/man/mann/pkg_mkIndex.n
/usr/share/man/mann/platform.n
/usr/share/man/mann/platform_shell.n
/usr/share/man/mann/proc.n
/usr/share/man/mann/puts.n
/usr/share/man/mann/pwd.n
/usr/share/man/mann/re_syntax.n
/usr/share/man/mann/read.n
/usr/share/man/mann/refchan.n
/usr/share/man/mann/regexp.n
/usr/share/man/mann/registry.n
/usr/share/man/mann/regsub.n
/usr/share/man/mann/rename.n
/usr/share/man/mann/return.n
/usr/share/man/mann/safe.n
/usr/share/man/mann/scan.n
/usr/share/man/mann/scope.n
/usr/share/man/mann/seek.n
/usr/share/man/mann/self.n
/usr/share/man/mann/set.n
/usr/share/man/mann/socket.n
/usr/share/man/mann/source.n
/usr/share/man/mann/split.n
/usr/share/man/mann/sqlite3.n
/usr/share/man/mann/string.n
/usr/share/man/mann/subst.n
/usr/share/man/mann/switch.n
/usr/share/man/mann/tailcall.n
/usr/share/man/mann/tcl_endOfWord.n
/usr/share/man/mann/tcl_findLibrary.n
/usr/share/man/mann/tcl_interactive.n
/usr/share/man/mann/tcl_library.n
/usr/share/man/mann/tcl_nonwordchars.n
/usr/share/man/mann/tcl_patchLevel.n
/usr/share/man/mann/tcl_pkgPath.n
/usr/share/man/mann/tcl_platform.n
/usr/share/man/mann/tcl_precision.n
/usr/share/man/mann/tcl_prefix.n
/usr/share/man/mann/tcl_rcFileName.n
/usr/share/man/mann/tcl_startOfNextWord.n
/usr/share/man/mann/tcl_startOfPreviousWord.n
/usr/share/man/mann/tcl_traceCompile.n
/usr/share/man/mann/tcl_traceExec.n
/usr/share/man/mann/tcl_version.n
/usr/share/man/mann/tcl_wordBreakAfter.n
/usr/share/man/mann/tcl_wordBreakBefore.n
/usr/share/man/mann/tcl_wordchars.n
/usr/share/man/mann/tcltest.n
/usr/share/man/mann/tdbc.n
/usr/share/man/mann/tdbc_connection.n
/usr/share/man/mann/tdbc_mapSqlState.n
/usr/share/man/mann/tdbc_mysql.n
/usr/share/man/mann/tdbc_odbc.n
/usr/share/man/mann/tdbc_resultset.n
/usr/share/man/mann/tdbc_sqlite3.n
/usr/share/man/mann/tdbc_statement.n
/usr/share/man/mann/tdbc_tokenize.n
/usr/share/man/mann/tell.n
/usr/share/man/mann/thread.n
/usr/share/man/mann/throw.n
/usr/share/man/mann/time.n
/usr/share/man/mann/tm.n
/usr/share/man/mann/tpool.n
/usr/share/man/mann/trace.n
/usr/share/man/mann/transchan.n
/usr/share/man/mann/try.n
/usr/share/man/mann/tsv.n
/usr/share/man/mann/ttrace.n
/usr/share/man/mann/unknown.n
/usr/share/man/mann/unload.n
/usr/share/man/mann/unset.n
/usr/share/man/mann/update.n
/usr/share/man/mann/uplevel.n
/usr/share/man/mann/upvar.n
/usr/share/man/mann/variable.n
/usr/share/man/mann/vwait.n
/usr/share/man/mann/while.n
/usr/share/man/mann/yield.n
/usr/share/man/mann/yieldto.n
/usr/share/man/mann/zlib.n

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.a
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/itcl*/libitcl*.so
/usr/lib64/sqlite*/libsqlite*.so
/usr/lib64/tdbc*/libtdbc*.so
/usr/lib64/tdbcmysql*/libtdbcmysql*.so
/usr/lib64/tdbcodbc*/libtdbcodbc*.so
/usr/lib64/tdbcpostgres*/libtdbcpostgres*.so
/usr/lib64/thread*/libthread*.so
