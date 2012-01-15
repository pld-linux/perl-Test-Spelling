#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Spelling
Summary:	Test::Spelling - check for spelling errors in POD files
Summary(pl.UTF-8):	Test::Spelling - sprawdzanie plików POD pod kątem błędów pisowni
Name:		perl-Test-Spelling
Version:	0.15
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f2713ff45abf1862e1edd45f72cf7ea1
URL:		http://search.cpan.org/dist/Test-Spelling/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Pod-Spell >= 1.01
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Check POD files for spelling mistakes, using Pod::Spell and spell to
do the heavy lifting.

%description -l pl.UTF-8
Ten moduł sprawdza pliki POD pod kątem błędów pisowni, wykorzystując
moduł Pod::Spell i polecenie spell.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/*.pm
%{_mandir}/man3/*
