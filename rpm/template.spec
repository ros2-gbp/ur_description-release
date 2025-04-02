%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-ur-description
Version:        3.1.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ur_description package

License:        BSD-3-Clause and Universal Robots A/S’ Terms and Conditions for Use of Graphical Documentation
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jazzy-joint-state-publisher-gui
Requires:       ros-jazzy-launch
Requires:       ros-jazzy-launch-ros
Requires:       ros-jazzy-robot-state-publisher
Requires:       ros-jazzy-rviz2
Requires:       ros-jazzy-urdf
Requires:       ros-jazzy-xacro
Requires:       ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-jazzy-ament-cmake-pytest
BuildRequires:  ros-jazzy-launch-testing-ament-cmake
BuildRequires:  ros-jazzy-launch-testing-ros
BuildRequires:  ros-jazzy-xacro
BuildRequires:  urdfdom
%endif

%description
URDF description for Universal Robots

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
%license LICENSE
%license meshes/ur20/LICENSE.txt
/opt/ros/jazzy

%changelog
* Wed Apr 02 2025 Felix Exner <feex@universal-robots.com> - 3.1.0-1
- Autogenerated by Bloom

* Mon Mar 17 2025 Felix Exner <feex@universal-robots.com> - 3.0.2-1
- Autogenerated by Bloom

* Thu Jan 23 2025 Felix Exner <feex@universal-robots.com> - 3.0.1-1
- Autogenerated by Bloom

* Wed Dec 11 2024 Felix Exner <exner@fzi.de> - 3.0.0-1
- Autogenerated by Bloom

* Mon Oct 14 2024 Felix Exner <exner@fzi.de> - 2.4.5-1
- Autogenerated by Bloom

* Wed Sep 11 2024 Felix Exner <exner@fzi.de> - 2.4.3-1
- Autogenerated by Bloom

* Sun Aug 11 2024 Felix Exner <exner@fzi.de> - 2.4.2-1
- Autogenerated by Bloom

* Mon Apr 29 2024 Felix Exner <exner@fzi.de> - 2.4.0-1
- Autogenerated by Bloom

* Fri Apr 19 2024 Felix Exner <exner@fzi.de> - 2.2.5-2
- Autogenerated by Bloom

* Thu Apr 04 2024 Felix Exner <exner@fzi.de> - 2.2.5-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Felix Exner <exner@fzi.de> - 2.2.4-2
- Autogenerated by Bloom

