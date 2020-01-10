Name: hunspell-quh
Summary: Quechua, South Bolivia hunspell dictionaries
%define upstreamid 20110816
Version: 0.%{upstreamid}
Release: 4%{?dist}
Source: http://www.runasimipi.org/quh_BO-pack.zip
Group: Applications/Text
URL: http://www.runasimipi.org/blanco-en.php?file=desarrollar-orto
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Quechua South Bolivia hunspell dictionaries.

%prep
%setup -q -n quh_BO-pack
unzip -qq quh_BO.zip

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p quh_BO/quh_BO.* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README quh_BO/COPYING quh_BO/Copyright quh_BO/README_quh_BO.txt
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110816-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110816-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110816-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 26 2011 Caolan McNamara <caolanm@redhat.com> - 0.20110816-1
- keep in sync

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081017-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Caolan McNamara <caolanm@redhat.com> - 0.20081017-1
- initial version
