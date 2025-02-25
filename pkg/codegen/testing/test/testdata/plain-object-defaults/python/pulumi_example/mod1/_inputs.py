# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'TypArgs',
]

@pulumi.input_type
class TypArgs:
    def __init__(__self__, *,
                 val: Optional[pulumi.Input[str]] = None):
        """
        A test for namespaces (mod 1)
        """
        TypArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            val=val,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             val: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if val is None:
            val = (_utilities.get_env('PULUMI_EXAMPLE_MOD1_DEFAULT') or 'mod1')
        if val is not None:
            _setter("val", val)

    @property
    @pulumi.getter
    def val(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "val")

    @val.setter
    def val(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "val", value)


