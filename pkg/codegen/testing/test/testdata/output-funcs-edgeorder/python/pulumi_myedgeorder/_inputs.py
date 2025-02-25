# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from ._enums import *

__all__ = [
    'ConfigurationFilters',
    'CustomerSubscriptionDetails',
    'CustomerSubscriptionRegisteredFeatures',
    'FilterableProperty',
    'HierarchyInformation',
]

@pulumi.input_type
class ConfigurationFilters:
    def __init__(__self__, *,
                 hierarchy_information: 'HierarchyInformation',
                 filterable_property: Optional[Sequence['FilterableProperty']] = None):
        """
        Configuration filters
        :param 'HierarchyInformation' hierarchy_information: Product hierarchy information
        :param Sequence['FilterableProperty'] filterable_property: Filters specific to product
        """
        ConfigurationFilters._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            hierarchy_information=hierarchy_information,
            filterable_property=filterable_property,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             hierarchy_information: 'HierarchyInformation',
             filterable_property: Optional[Sequence['FilterableProperty']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("hierarchy_information", hierarchy_information)
        if filterable_property is not None:
            _setter("filterable_property", filterable_property)

    @property
    @pulumi.getter(name="hierarchyInformation")
    def hierarchy_information(self) -> 'HierarchyInformation':
        """
        Product hierarchy information
        """
        return pulumi.get(self, "hierarchy_information")

    @hierarchy_information.setter
    def hierarchy_information(self, value: 'HierarchyInformation'):
        pulumi.set(self, "hierarchy_information", value)

    @property
    @pulumi.getter(name="filterableProperty")
    def filterable_property(self) -> Optional[Sequence['FilterableProperty']]:
        """
        Filters specific to product
        """
        return pulumi.get(self, "filterable_property")

    @filterable_property.setter
    def filterable_property(self, value: Optional[Sequence['FilterableProperty']]):
        pulumi.set(self, "filterable_property", value)


@pulumi.input_type
class CustomerSubscriptionDetails:
    def __init__(__self__, *,
                 quota_id: str,
                 location_placement_id: Optional[str] = None,
                 registered_features: Optional[Sequence['CustomerSubscriptionRegisteredFeatures']] = None):
        """
        Holds Customer subscription details. Clients can display available products to unregistered customers by explicitly passing subscription details
        :param str quota_id: Quota ID of a subscription
        :param str location_placement_id: Location placement Id of a subscription
        :param Sequence['CustomerSubscriptionRegisteredFeatures'] registered_features: List of registered feature flags for subscription
        """
        CustomerSubscriptionDetails._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            quota_id=quota_id,
            location_placement_id=location_placement_id,
            registered_features=registered_features,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             quota_id: str,
             location_placement_id: Optional[str] = None,
             registered_features: Optional[Sequence['CustomerSubscriptionRegisteredFeatures']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("quota_id", quota_id)
        if location_placement_id is not None:
            _setter("location_placement_id", location_placement_id)
        if registered_features is not None:
            _setter("registered_features", registered_features)

    @property
    @pulumi.getter(name="quotaId")
    def quota_id(self) -> str:
        """
        Quota ID of a subscription
        """
        return pulumi.get(self, "quota_id")

    @quota_id.setter
    def quota_id(self, value: str):
        pulumi.set(self, "quota_id", value)

    @property
    @pulumi.getter(name="locationPlacementId")
    def location_placement_id(self) -> Optional[str]:
        """
        Location placement Id of a subscription
        """
        return pulumi.get(self, "location_placement_id")

    @location_placement_id.setter
    def location_placement_id(self, value: Optional[str]):
        pulumi.set(self, "location_placement_id", value)

    @property
    @pulumi.getter(name="registeredFeatures")
    def registered_features(self) -> Optional[Sequence['CustomerSubscriptionRegisteredFeatures']]:
        """
        List of registered feature flags for subscription
        """
        return pulumi.get(self, "registered_features")

    @registered_features.setter
    def registered_features(self, value: Optional[Sequence['CustomerSubscriptionRegisteredFeatures']]):
        pulumi.set(self, "registered_features", value)


@pulumi.input_type
class CustomerSubscriptionRegisteredFeatures:
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 state: Optional[str] = None):
        """
        Represents subscription registered features
        :param str name: Name of subscription registered feature
        :param str state: State of subscription registered feature
        """
        CustomerSubscriptionRegisteredFeatures._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            state=state,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[str] = None,
             state: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if name is not None:
            _setter("name", name)
        if state is not None:
            _setter("state", state)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of subscription registered feature
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        State of subscription registered feature
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[str]):
        pulumi.set(self, "state", value)


@pulumi.input_type
class FilterableProperty:
    def __init__(__self__, *,
                 supported_values: Sequence[str],
                 type: Union[str, 'SupportedFilterTypes']):
        """
        Different types of filters supported and its values.
        :param Sequence[str] supported_values: Values to be filtered.
        :param Union[str, 'SupportedFilterTypes'] type: Type of product filter.
        """
        FilterableProperty._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            supported_values=supported_values,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             supported_values: Sequence[str],
             type: Union[str, 'SupportedFilterTypes'],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("supported_values", supported_values)
        _setter("type", type)

    @property
    @pulumi.getter(name="supportedValues")
    def supported_values(self) -> Sequence[str]:
        """
        Values to be filtered.
        """
        return pulumi.get(self, "supported_values")

    @supported_values.setter
    def supported_values(self, value: Sequence[str]):
        pulumi.set(self, "supported_values", value)

    @property
    @pulumi.getter
    def type(self) -> Union[str, 'SupportedFilterTypes']:
        """
        Type of product filter.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Union[str, 'SupportedFilterTypes']):
        pulumi.set(self, "type", value)


@pulumi.input_type
class HierarchyInformation:
    def __init__(__self__, *,
                 configuration_name: Optional[str] = None,
                 product_family_name: Optional[str] = None,
                 product_line_name: Optional[str] = None,
                 product_name: Optional[str] = None):
        """
        Holds details about product hierarchy information
        :param str configuration_name: Represents configuration name that uniquely identifies configuration
        :param str product_family_name: Represents product family name that uniquely identifies product family
        :param str product_line_name: Represents product line name that uniquely identifies product line
        :param str product_name: Represents product name that uniquely identifies product
        """
        HierarchyInformation._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            configuration_name=configuration_name,
            product_family_name=product_family_name,
            product_line_name=product_line_name,
            product_name=product_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             configuration_name: Optional[str] = None,
             product_family_name: Optional[str] = None,
             product_line_name: Optional[str] = None,
             product_name: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if configuration_name is not None:
            _setter("configuration_name", configuration_name)
        if product_family_name is not None:
            _setter("product_family_name", product_family_name)
        if product_line_name is not None:
            _setter("product_line_name", product_line_name)
        if product_name is not None:
            _setter("product_name", product_name)

    @property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> Optional[str]:
        """
        Represents configuration name that uniquely identifies configuration
        """
        return pulumi.get(self, "configuration_name")

    @configuration_name.setter
    def configuration_name(self, value: Optional[str]):
        pulumi.set(self, "configuration_name", value)

    @property
    @pulumi.getter(name="productFamilyName")
    def product_family_name(self) -> Optional[str]:
        """
        Represents product family name that uniquely identifies product family
        """
        return pulumi.get(self, "product_family_name")

    @product_family_name.setter
    def product_family_name(self, value: Optional[str]):
        pulumi.set(self, "product_family_name", value)

    @property
    @pulumi.getter(name="productLineName")
    def product_line_name(self) -> Optional[str]:
        """
        Represents product line name that uniquely identifies product line
        """
        return pulumi.get(self, "product_line_name")

    @product_line_name.setter
    def product_line_name(self, value: Optional[str]):
        pulumi.set(self, "product_line_name", value)

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> Optional[str]:
        """
        Represents product name that uniquely identifies product
        """
        return pulumi.get(self, "product_name")

    @product_name.setter
    def product_name(self, value: Optional[str]):
        pulumi.set(self, "product_name", value)


