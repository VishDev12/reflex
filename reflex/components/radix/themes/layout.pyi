"""Stub file for layout.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, List, Optional, Union, overload
from reflex.components.radix.themes.base import CommonMarginProps
from reflex.components.component import Component
from reflex.components.radix.themes.base import RadixThemesComponent
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventHandler, EventChain, EventSpec
from reflex.style import Style

class LayoutComponent(CommonMarginProps, RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        p: Optional[Union[Var[str], str]] = None,
        px: Optional[Union[Var[str], str]] = None,
        py: Optional[Union[Var[str], str]] = None,
        pt: Optional[Union[Var[str], str]] = None,
        pr: Optional[Union[Var[str], str]] = None,
        pb: Optional[Union[Var[str], str]] = None,
        pl: Optional[Union[Var[str], str]] = None,
        shrink: Optional[Union[Var[str], str]] = None,
        grow: Optional[Union[Var[str], str]] = None,
        m: Optional[Union[Var[str], str]] = None,
        mx: Optional[Union[Var[str], str]] = None,
        my: Optional[Union[Var[str], str]] = None,
        mt: Optional[Union[Var[str], str]] = None,
        mr: Optional[Union[Var[str], str]] = None,
        mb: Optional[Union[Var[str], str]] = None,
        ml: Optional[Union[Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, str]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        **props
    ) -> "LayoutComponent":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            p: Padding: "0" - "9"
            px: Padding horizontal: "0" - "9"
            py: Padding vertical: "0" - "9"
            pt: Padding top: "0" - "9"
            pr: Padding right: "0" - "9"
            pb: Padding bottom: "0" - "9"
            pl: Padding left: "0" - "9"
            shrink: Whether the element will take up the smallest possible space: "0" | "1"
            grow: Whether the element will take up the largest possible space: "0" | "1"
            m: Margin: "0" - "9"
            mx: Margin horizontal: "0" - "9"
            my: Margin vertical: "0" - "9"
            mt: Margin top: "0" - "9"
            mr: Margin right: "0" - "9"
            mb: Margin bottom: "0" - "9"
            ml: Margin left: "0" - "9"
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

class Box(LayoutComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        p: Optional[Union[Var[str], str]] = None,
        px: Optional[Union[Var[str], str]] = None,
        py: Optional[Union[Var[str], str]] = None,
        pt: Optional[Union[Var[str], str]] = None,
        pr: Optional[Union[Var[str], str]] = None,
        pb: Optional[Union[Var[str], str]] = None,
        pl: Optional[Union[Var[str], str]] = None,
        shrink: Optional[Union[Var[str], str]] = None,
        grow: Optional[Union[Var[str], str]] = None,
        m: Optional[Union[Var[str], str]] = None,
        mx: Optional[Union[Var[str], str]] = None,
        my: Optional[Union[Var[str], str]] = None,
        mt: Optional[Union[Var[str], str]] = None,
        mr: Optional[Union[Var[str], str]] = None,
        mb: Optional[Union[Var[str], str]] = None,
        ml: Optional[Union[Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, str]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        **props
    ) -> "Box":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            p: Padding: "0" - "9"
            px: Padding horizontal: "0" - "9"
            py: Padding vertical: "0" - "9"
            pt: Padding top: "0" - "9"
            pr: Padding right: "0" - "9"
            pb: Padding bottom: "0" - "9"
            pl: Padding left: "0" - "9"
            shrink: Whether the element will take up the smallest possible space: "0" | "1"
            grow: Whether the element will take up the largest possible space: "0" | "1"
            m: Margin: "0" - "9"
            mx: Margin horizontal: "0" - "9"
            my: Margin vertical: "0" - "9"
            mt: Margin top: "0" - "9"
            mr: Margin right: "0" - "9"
            mb: Margin bottom: "0" - "9"
            ml: Margin left: "0" - "9"
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

class Flex(LayoutComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        as_child: Optional[Union[Var[bool], bool]] = None,
        display: Optional[Union[Var[str], str]] = None,
        direction: Optional[Union[Var[str], str]] = None,
        align: Optional[Union[Var[str], str]] = None,
        justify: Optional[Union[Var[str], str]] = None,
        wrap: Optional[Union[Var[str], str]] = None,
        gap: Optional[Union[Var[str], str]] = None,
        p: Optional[Union[Var[str], str]] = None,
        px: Optional[Union[Var[str], str]] = None,
        py: Optional[Union[Var[str], str]] = None,
        pt: Optional[Union[Var[str], str]] = None,
        pr: Optional[Union[Var[str], str]] = None,
        pb: Optional[Union[Var[str], str]] = None,
        pl: Optional[Union[Var[str], str]] = None,
        shrink: Optional[Union[Var[str], str]] = None,
        grow: Optional[Union[Var[str], str]] = None,
        m: Optional[Union[Var[str], str]] = None,
        mx: Optional[Union[Var[str], str]] = None,
        my: Optional[Union[Var[str], str]] = None,
        mt: Optional[Union[Var[str], str]] = None,
        mr: Optional[Union[Var[str], str]] = None,
        mb: Optional[Union[Var[str], str]] = None,
        ml: Optional[Union[Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, str]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        **props
    ) -> "Flex":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            as_child: Change the default rendered element for the one passed as a child, merging their props and behavior.
            display: How to display the element: "none" | "inline-flex" | "flex"
            direction: How child items are layed out: "row" | "column" | "row-reverse" | "column-reverse"
            align: Alignment of children along the main axis: "start" | "center" | "end" | "baseline" | "stretch"
            justify: Alignment of children along the cross axis: "start" | "center" | "end" | "between"
            wrap: Whether children should wrap when they reach the end of their container: "nowrap" | "wrap" | "wrap-reverse"
            gap: Gap between children: "0" - "9"
            p: Padding: "0" - "9"
            px: Padding horizontal: "0" - "9"
            py: Padding vertical: "0" - "9"
            pt: Padding top: "0" - "9"
            pr: Padding right: "0" - "9"
            pb: Padding bottom: "0" - "9"
            pl: Padding left: "0" - "9"
            shrink: Whether the element will take up the smallest possible space: "0" | "1"
            grow: Whether the element will take up the largest possible space: "0" | "1"
            m: Margin: "0" - "9"
            mx: Margin horizontal: "0" - "9"
            my: Margin vertical: "0" - "9"
            mt: Margin top: "0" - "9"
            mr: Margin right: "0" - "9"
            mb: Margin bottom: "0" - "9"
            ml: Margin left: "0" - "9"
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

class Grid(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        as_child: Optional[Union[Var[bool], bool]] = None,
        display: Optional[Union[Var[str], str]] = None,
        columns: Optional[Union[Var[str], str]] = None,
        rows: Optional[Union[Var[str], str]] = None,
        flow: Optional[Union[Var[str], str]] = None,
        align: Optional[Union[Var[str], str]] = None,
        justify: Optional[Union[Var[str], str]] = None,
        gap: Optional[Union[Var[str], str]] = None,
        gap_x: Optional[Union[Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, str]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        **props
    ) -> "Grid":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            as_child: Change the default rendered element for the one passed as a child, merging their props and behavior.
            display: How to display the element: "none" | "inline-grid" | "grid"
            columns: Number of columns
            rows: Number of rows
            flow: How the grid items are layed out: "row" | "column" | "dense" | "row-dense" | "column-dense"
            align: Alignment of children along the main axis: "start" | "center" | "end" | "baseline" | "stretch"
            justify: Alignment of children along the cross axis: "start" | "center" | "end" | "between"
            gap: Gap between children: "0" - "9"
            gap_x: Gap between children vertical: "0" - "9"
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

class Container(LayoutComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        size: Optional[Union[Var[str], str]] = None,
        p: Optional[Union[Var[str], str]] = None,
        px: Optional[Union[Var[str], str]] = None,
        py: Optional[Union[Var[str], str]] = None,
        pt: Optional[Union[Var[str], str]] = None,
        pr: Optional[Union[Var[str], str]] = None,
        pb: Optional[Union[Var[str], str]] = None,
        pl: Optional[Union[Var[str], str]] = None,
        shrink: Optional[Union[Var[str], str]] = None,
        grow: Optional[Union[Var[str], str]] = None,
        m: Optional[Union[Var[str], str]] = None,
        mx: Optional[Union[Var[str], str]] = None,
        my: Optional[Union[Var[str], str]] = None,
        mt: Optional[Union[Var[str], str]] = None,
        mr: Optional[Union[Var[str], str]] = None,
        mb: Optional[Union[Var[str], str]] = None,
        ml: Optional[Union[Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, str]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        **props
    ) -> "Container":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            size: The size of the container: "1" - "4" (default "4")
            p: Padding: "0" - "9"
            px: Padding horizontal: "0" - "9"
            py: Padding vertical: "0" - "9"
            pt: Padding top: "0" - "9"
            pr: Padding right: "0" - "9"
            pb: Padding bottom: "0" - "9"
            pl: Padding left: "0" - "9"
            shrink: Whether the element will take up the smallest possible space: "0" | "1"
            grow: Whether the element will take up the largest possible space: "0" | "1"
            m: Margin: "0" - "9"
            mx: Margin horizontal: "0" - "9"
            my: Margin vertical: "0" - "9"
            mt: Margin top: "0" - "9"
            mr: Margin right: "0" - "9"
            mb: Margin bottom: "0" - "9"
            ml: Margin left: "0" - "9"
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

class Section(LayoutComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        size: Optional[Union[Var[str], str]] = None,
        p: Optional[Union[Var[str], str]] = None,
        px: Optional[Union[Var[str], str]] = None,
        py: Optional[Union[Var[str], str]] = None,
        pt: Optional[Union[Var[str], str]] = None,
        pr: Optional[Union[Var[str], str]] = None,
        pb: Optional[Union[Var[str], str]] = None,
        pl: Optional[Union[Var[str], str]] = None,
        shrink: Optional[Union[Var[str], str]] = None,
        grow: Optional[Union[Var[str], str]] = None,
        m: Optional[Union[Var[str], str]] = None,
        mx: Optional[Union[Var[str], str]] = None,
        my: Optional[Union[Var[str], str]] = None,
        mt: Optional[Union[Var[str], str]] = None,
        mr: Optional[Union[Var[str], str]] = None,
        mb: Optional[Union[Var[str], str]] = None,
        ml: Optional[Union[Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, str]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        **props
    ) -> "Section":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            size: The size of the section: "1" - "3" (default "3")
            p: Padding: "0" - "9"
            px: Padding horizontal: "0" - "9"
            py: Padding vertical: "0" - "9"
            pt: Padding top: "0" - "9"
            pr: Padding right: "0" - "9"
            pb: Padding bottom: "0" - "9"
            pl: Padding left: "0" - "9"
            shrink: Whether the element will take up the smallest possible space: "0" | "1"
            grow: Whether the element will take up the largest possible space: "0" | "1"
            m: Margin: "0" - "9"
            mx: Margin horizontal: "0" - "9"
            my: Margin vertical: "0" - "9"
            mt: Margin top: "0" - "9"
            mr: Margin right: "0" - "9"
            mb: Margin bottom: "0" - "9"
            ml: Margin left: "0" - "9"
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...
