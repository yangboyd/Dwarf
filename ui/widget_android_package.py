"""
Dwarf - Copyright (C) 2018 iGio90

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>
"""
from ui.widget_item_not_editable import NotEditableListWidgetItem


class AndroidPackageWidget(NotEditableListWidgetItem):
    def __init__(self, android_package):
        super().__init__(android_package.package)

        self.android_package = android_package

    def get_android_package(self):
        return self.android_package
