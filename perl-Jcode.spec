#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	Jcode
Summary:	Jcode - Japanese charset handler
Summary(pl):	Jcode - obsługa kodowania japońskiego
Name:		perl-Jcode
Version:	0.83
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/D/DA/DANKOGAI/%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-MIME-Base64
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jcode is a Perl extension interface to convert Japanese text.

%description -l pl
Jcode jest rozszerzeniem Perla do konwersji tekstu japońskiego.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%dir %{perl_sitearch}/Jcode
%{perl_sitearch}/*.pm
%{perl_sitearch}/Jcode/*.pm
%{perl_sitearch}/Jcode/Unicode
%dir %{perl_sitearch}/auto/Jcode
%dir %{perl_sitearch}/auto/Jcode/Unicode
%attr(755,root,root) %{perl_sitearch}/auto/Jcode/Unicode/*.so
%{perl_sitearch}/auto/Jcode/Unicode/*.bs
%{_mandir}/man3/*
