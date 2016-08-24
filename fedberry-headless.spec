%define bname   fedberry
%define name    %{bname}-headless

Name:       %{name}
Version:    0.1
Release:    1%{?dist}
License:    GPLv3+
Summary:    Boot your Raspberry Pi using headless mode.
Group:      Applications/System
URL:        https://github.com/${bname}/%{name}
Source0:    https://raw.githubusercontent.com/%{bname}/%{name}/master/headless
Source1:    https://raw.githubusercontent.com/%{bname}/%{name}/master/headless-check.service
BuildArch:  noarch
BuildRequires: systemd-units
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
Headless mode disables the initial-setup service and obtains an ip-address through dhcp or assigns a static ip-address using information provided in the /boot/headless file.


%prep
%setup -c -T
cp -a %{SOURCE0} %{SOURCE1} .


%build


%install
rm -rf %{buildroot}

%{__install} -d %{buildroot}/%{_sbindir}
%{__install} -p headless %{buildroot}/%{_sbindir}

%{__install} -d %{buildroot}/%{_unitdir}
%{__install} -p headless-check.service %{buildroot}/%{_unitdir}


%clean
rm -rf %{buildroot}


%post
%systemd_post headless-check.service


%preun
%systemd_preun headless-check.service


%postun
%systemd_postun headless-check.service


%files
%attr(0755,root,root) %{_sbindir}/headless
%attr(0644,root,root) %{_unitdir}/headless-check.service


%changelog
* Wed Aug 24 2016 Vaughan <vaughan at agrez dot net> 0.1-1
- Initial package
