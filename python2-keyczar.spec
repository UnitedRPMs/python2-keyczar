Name:           python2-keyczar
Version:        0.716
Release:        7%{?dist}
Summary:        Toolkit for safe and simple cryptography

Group:          Development/Languages
License:        ASL 2.0
URL:            http://www.keyczar.org/
Source0:        https://files.pythonhosted.org/packages/c8/14/3ffb68671fef927fa5b60f21c43a04a4a007acbe939a26ba08b197fea6b3/python-keyczar-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2
BuildRequires:  python2-devel
#
BuildRequires:  python2-crypto
BuildRequires:  python2-pyasn1
#

Requires:       python2-crypto
Requires:       python2-pyasn1

%description
Keyczar is an open source cryptographic toolkit designed to make it easier and
safer for developers to use cryptography in their applications. Keyczar
supports authentication and encryption with both symmetric and asymmetric keys.


%prep
%autosetup -n python-keyczar-%{version}

%build
/usr/bin/python2 setup.py build

%install
/usr/bin/python2 setup.py install --root %{buildroot} --optimize=1

%files
%doc README LICENSE doc/pycrypt.pdf
%{_bindir}/keyczart
%{python2_sitelib}/keyczar/
%{python2_sitelib}/python_keyczar-*.egg-info

%changelog

* Tue Feb 19 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.716-7
- Updated to 0.716
- Upstream

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.71c-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.71c-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71c-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.71c-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71c-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71c-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71c-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 - Maxim Burgerhout <wzzrd@fedoraproject.org> - 0.71c-1
- Build with new upstream tarball containing fixes for hashbangs, exec bits,
  a LICENSE file and more.

* Mon Dec 10 2012 - Maxim Burgerhout <wzzrd@fedoraproject.org> - 0.71b-2
- Enable tests to be run during build
- Remove EL5 code from specfile in order to 
- Fix %%files section to include the proper files

* Sun Dec 9 2012 - Maxim Burgerhout <wzzrd@fedoraproject.org> - 0.71b-1
- Initial build of 0.71b for Fedora
