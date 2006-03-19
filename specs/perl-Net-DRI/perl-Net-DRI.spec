# $Id$
# Authority: dries
# Upstream: Patrick Mevzek <patrick$deepcore,org>

%define real_name Net-DRI
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Uniform API to access domain registries, registrars and resellers
Name: perl-Net-DRI
Version: 0.21
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DRI/

Source: http://search.cpan.org/CPAN/authors/id/P/PM/PMEVZEK/Net-DRI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Net::DRI is a Perl library which offers a uniform API to access services 
from domain name registries, registrars, and resellers. It is an 
object-oriented framework that can be easily extended to handle various 
protocols (such as RRP, EPP, or custom protocols) and various transports 
methods (such as TCP, TLS, SOAP, or email).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Net::DRI*
%{perl_vendorlib}/Net/DRI.pm
%{perl_vendorlib}/Net/DRI/

%changelog
* Tue Mar 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Updated to release 0.21.

* Tue Nov 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Updated to release 0.19.

* Tue Nov 08 2005 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Initial package.
