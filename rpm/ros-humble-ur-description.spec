%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-ur-description
Version:        2.1.3
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ur_description package

License:        BSD-3-Clause and Universal Robots A/S’ Terms and Conditions for Use of Graphical Documentation
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-joint-state-publisher-gui
Requires:       ros-humble-launch
Requires:       ros-humble-launch-ros
Requires:       ros-humble-robot-state-publisher
Requires:       ros-humble-rviz2
Requires:       ros-humble-urdf
Requires:       ros-humble-xacro
Requires:       ros-humble-ros-workspace
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-cmake-pytest
BuildRequires:  ros-humble-launch-testing-ament-cmake
BuildRequires:  ros-humble-launch-testing-ros
BuildRequires:  ros-humble-xacro
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
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
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
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
%license LICENSE
%license meshes/ur20/LICENSE.txt
/opt/ros/humble

%changelog
* Thu Dec 21 2023 Felix Exner <exner@fzi.de> - 2.1.3-1
- Autogenerated by Bloom

* Wed Dec 13 2023 Felix Exner <exner@fzi.de> - 2.1.2-1
- Autogenerated by Bloom

* Mon Sep 11 2023 Felix Exner <exner@fzi.de> - 2.1.1-1
- Autogenerated by Bloom

* Thu Jun 01 2023 Felix Exner <exner@fzi.de> - 2.1.0-1
- Autogenerated by Bloom

* Tue Nov 08 2022 Felix Exner <exner@fzi.de> - 2.0.1-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Felix Exner <exner@fzi.de> - 2.0.0-2
- Autogenerated by Bloom

* Wed Mar 30 2022 Felix Exner <exner@fzi.de> - 2.0.0-1
- Autogenerated by Bloom
