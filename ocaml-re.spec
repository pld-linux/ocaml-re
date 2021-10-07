#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

%define		module	re
Summary:	Regular expression library for OCaml
Summary(pl.UTF-8):	Biblioteka wyrażeń regularnych dla OCamla
Name:		ocaml-re
Version:	1.10.3
Release:	1
License:	LGPL v2.1 with linking exception
Group:		Libraries
#Source0Download: https://github.com/ocaml/ocaml-re/releases
Source0:	https://github.com/ocaml/ocaml-re/releases/download/%{version}/re-%{version}.tbz
# Source0-md5:	a36347dcfaf71c95916f96f72b0cf2ce
URL:		https://github.com/ocaml/ocaml-re
#BuildRequires:	-devel
BuildRequires:	ocaml >= 1:4.02
BuildRequires:	ocaml-dune >= 2.0
BuildRequires:	ocaml-seq-devel
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
RE is a regular expression library for OCaml.

This package contains files needed to run bytecode executables using
re library.

%description -l pl.UTF-8
RE to biblioteka wyrażeń regularnych dla OCamla.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki re.

%package devel
Summary:	Regular expression library for OCaml - development part
Summary(pl.UTF-8):	Biblioteka wyrażeń regularnych dla OCamla - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ocaml-seq-devel
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using re
library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki re.

%prep
%setup -q -n re-%{version}

%build
dune build -p re --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install -p re --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/re/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/re/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/re

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md TODO.txt
%dir %{_libdir}/ocaml/re
%{_libdir}/ocaml/re/META
%{_libdir}/ocaml/re/*.cma
%dir %{_libdir}/ocaml/re/emacs
%{_libdir}/ocaml/re/emacs/*.cma
%dir %{_libdir}/ocaml/re/glob
%{_libdir}/ocaml/re/glob/*.cma
%dir %{_libdir}/ocaml/re/pcre
%{_libdir}/ocaml/re/pcre/*.cma
%dir %{_libdir}/ocaml/re/perl
%{_libdir}/ocaml/re/perl/*.cma
%dir %{_libdir}/ocaml/re/posix
%{_libdir}/ocaml/re/posix/*.cma
%dir %{_libdir}/ocaml/re/str
%{_libdir}/ocaml/re/str/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/re/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/re/emacs/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/re/glob/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/re/pcre/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/re/perl/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/re/posix/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/re/str/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/re/*.cmi
%{_libdir}/ocaml/re/*.cmt
%{_libdir}/ocaml/re/*.cmti
%{_libdir}/ocaml/re/*.mli
%{_libdir}/ocaml/re/emacs/*.cmi
%{_libdir}/ocaml/re/emacs/*.cmt
%{_libdir}/ocaml/re/glob/*.cmi
%{_libdir}/ocaml/re/glob/*.cmt
%{_libdir}/ocaml/re/pcre/*.cmi
%{_libdir}/ocaml/re/pcre/*.cmt
%{_libdir}/ocaml/re/perl/*.cmi
%{_libdir}/ocaml/re/perl/*.cmt
%{_libdir}/ocaml/re/posix/*.cmi
%{_libdir}/ocaml/re/posix/*.cmt
%{_libdir}/ocaml/re/str/*.cmi
%{_libdir}/ocaml/re/str/*.cmt
%if %{with ocaml_opt}
%{_libdir}/ocaml/re/*.a
%{_libdir}/ocaml/re/*.cmx
%{_libdir}/ocaml/re/*.cmxa
%{_libdir}/ocaml/re/emacs/*.a
%{_libdir}/ocaml/re/emacs/*.cmx
%{_libdir}/ocaml/re/emacs/*.cmxa
%{_libdir}/ocaml/re/glob/*.a
%{_libdir}/ocaml/re/glob/*.cmx
%{_libdir}/ocaml/re/glob/*.cmxa
%{_libdir}/ocaml/re/pcre/*.a
%{_libdir}/ocaml/re/pcre/*.cmx
%{_libdir}/ocaml/re/pcre/*.cmxa
%{_libdir}/ocaml/re/perl/*.a
%{_libdir}/ocaml/re/perl/*.cmx
%{_libdir}/ocaml/re/perl/*.cmxa
%{_libdir}/ocaml/re/posix/*.a
%{_libdir}/ocaml/re/posix/*.cmx
%{_libdir}/ocaml/re/posix/*.cmxa
%{_libdir}/ocaml/re/str/*.a
%{_libdir}/ocaml/re/str/*.cmx
%{_libdir}/ocaml/re/str/*.cmxa
%endif
%{_libdir}/ocaml/re/dune-package
%{_libdir}/ocaml/re/opam
