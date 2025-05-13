# https://github.com/intel/numatop/pull/53
%undefine _ld_as_needed

Name:           numatop
Version:        2.4
Release:        6%{?dist}
Summary:        Memory access locality characterization and analysis

License:        BSD
URL:            https://01.org/numatop
Source:         https://github.com/intel/numatop/archive/refs/tags/v%{version}.tar.gz
# Patch0:         format.patch
Patch01:	0001-common-reg.c-use-explicit-format-string.patch
Patch02:	0002-numatop-powerpc-Add-Power11-support.patch
Patch03:	0003-add-required-SECURITY.md-file-for-OSSF-Scorecard-com.patch
Patch04:	0004-x86-zen-Add-Zen-5-and-later-support.patch
Patch05:	0005-readme-Add-note-on-AMD-support.patch
Patch06:	0006-Fix-several-printf-format-specifiers.patch
Patch07:	0007-Clean-up-32-bit-build-warnings.patch
Patch08:	0008-common-os-os_win.c-Fix-incorrect-usage-of-strncat.patch
Patch09:	0009-common-os-os_util.c-Fix-off-by-one-on-string-length-.patch
#Patch10:	0010-common-reg-Add-pragmas-to-silence-false-positive-war.patch
Patch11:	0011-x86-Fix-missing-fields-for-EMR-support.patch
Patch12:	0012-common-Use-sym_type_t-in-elf64_binary_read-signature.patch
Patch13:	0013-common-Remove-unnecessary-temp-buffer.patch
Patch14:	0014-common-Use-memcpy-to-the-process-name-to-a-line.patch
Patch15:	0015-common-Increase-node-string-buffer-size.patch
Patch16:	0016-Fix-remaining-clang-warnings.patch
#Patch17:	0017-Revert-common-reg-Add-pragmas-to-silence-false-posit.patch
Patch18:	0018-common-Replace-malloc-strncpy-with-strdup.patch
Patch19:	0019-common-Build-node-string-with-bound-checks.patch
Patch20:	0020-Add-missing-hunks-from-last-change.patch
Patch21:	0021-common-remove-extra-d-from-debug_print-and-fix-gramm.patch
Patch22:	0022-common-fix-uninitialized-string-content-in-dyn-pid-0.patch
Patch23:	0023-common-Add-missing-t-from-help-and-manual.patch
Patch24:	0024-common-perform-sanity-check-on-num-to-avoid-array-bo.patch
Patch25:	0025-common-ensure-the-dump-and-log-files-are-not-opened-.patch
Patch26:	0026-common-cast-difference-of-data_head-and-data_tail-to.patch
Patch27:	0027-common-resolve_unique-Fix-uninitialised-return-of-po.patch
Patch28:	0028-common-fix-timeout-option-break-out-of-loop.patch
Patch29:	0029-common-use-mount-umount-system-calls-rather-than-usi.patch
Patch30:	0030-common-remove-executing-commands-for-directory-and-f.patch
Patch31:	0031-powerpc-util-fix-build-warning-cast-LHS-of-expressio.patch
Patch32:	0032-common-os-map-Fix-overflow-warning.patch
Patch33:	0033-Move-all-curses-calls-into-display-threads.patch
Patch34:	0034-Avoid-race-on-submitting-display-commands.patch
Patch35:	0035-Remove-EMR-specific-events-configuration.patch
Patch36:	0036-Support-Intel-Granite-Rapids-platform.patch
Patch37:	0037-Support-Intel-Sierra-Forest-platform.patch



BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  check-devel
BuildRequires:  ncurses-devel
BuildRequires:  numactl-devel

# This only works for Intel and Power CPUs
ExclusiveArch:  x86_64 ppc64le

#Patch001: v2.2-001-Initial-support-for-SPR.patch


%description
NumaTOP is an observation tool for runtime memory locality characterization and
analysis of processes and threads running on a NUMA system. It helps the user
characterize the NUMA behavior of processes and threads and identify where the
NUMA-related performance bottlenecks reside.

NumaTOP supports the Intel Xeon processors and PowerPC processors.


%prep
#%setup -q -n %{name}-v%{version}
%autosetup -p1


%build
autoreconf --force --install --symlink
%configure
%make_build


%install
%make_install


%check
%make_build check


%files
%doc AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*


%changelog
* Thu Jan  2 2025 Pingfan Liu <piliu@redhat.com> - 2.4.6
- Add support for intel  GNR and SRF

* Thu Jan  2 2025 Pingfan Liu <piliu@redhat.com> - 2.4.5
- Fix ncures race issue

* Thu Feb  1 2024 Pingfan Liu <piliu@redhat.com> - 2.4.1
- Add initial support for EMR

* Fri Dec  8 2023 Pingfan Liu <piliu@redhat.com> - 2.3.3
- Add Power10 support

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 2.1-7
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.1-6
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 23 2019 Dridi Boukelmoune <dridi@fedoraproject.org>- 2.1-1
- Update to 2.1
- Upstream moved to github
- Upstream switched to autotools
- Disable --as-needed until it's patched upstream
- Drop defunct 32bit x86 support
- Add ppc64le support
- Run the new test suite

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Dridi Boukelmoune <dridi@fedoraproject.org>- 1.0.4-8
- Build requires gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Dridi Boukelmoune <dridi@fedoraproject.org>- 1.0.4-3
- Catch up with packaging guidelines

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 28 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.4-1
- Update to latest version (support for BDW-EP/EX)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 14 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.3-3
- Replace ExcludeArch with ExclusiveArch

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 25 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.3-1
- New upstream release (#1076549)
- Remove upstreamed patch

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.2-3
- Backport and rebase 1.0.1 patch

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 16 2014 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.2-1
- Bump version to 1.0.2
- Remove upstreamed patch

* Fri Sep 20 2013 Dan Horák <dan[at]danny.cz> - 1.0.1-5
- no numa on s390(x)

* Fri Sep 13 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.1-4
- Patch for the 32bit hardened build.

* Sun Aug 25 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.1-3
- Hardened build.
- Automatic requires.

* Fri Aug 02 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.1-2
- Fix the license tag.

* Thu Aug 01 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.1-1
- Initial spec.
