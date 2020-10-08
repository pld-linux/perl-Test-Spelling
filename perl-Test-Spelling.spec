#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define	pdir	Test
%define	pnam	Spelling
Summary:	Test::Spelling - check for spelling errors in POD files
Summary(pl.UTF-8):	Test::Spelling - sprawdzanie plików POD pod kątem błędów pisowni
Name:		perl-Test-Spelling
Version:	0.25
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5267be55736620cf8c45765e346a58cc
URL:		https://metacpan.org/release/Test-Spelling
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-IPC-Run3 >= 0.044
BuildRequires:	perl-Pod-Spell >= 1.01
BuildRequires:	perl-Test-Simple >= 0.88
BuildRequires:	perl-Test-Tester
%endif
Requires:	perl-IPC-Run3 >= 0.044
Requires:	perl-Pod-Spell >= 1.01
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
%{perl_vendorlib}/Test/Spelling.pm
%{_mandir}/man3/Test::Spelling.3pm*
