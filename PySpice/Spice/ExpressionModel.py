#!/usr/bin/env python

# CAVEAT UTILITOR
#
# This file was automatically generated by TatSu.
#
#    https://pypi.python.org/pypi/tatsu/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.

from __future__ import annotations

from typing import Any
from dataclasses import dataclass

from tatsu.objectmodel import Node
from tatsu.semantics import ModelBuilderSemantics


@dataclass(eq=False)
class ModelBase(Node):
    pass


class ExpressionModelBuilderSemantics(ModelBuilderSemantics):
    def __init__(self, context=None, types=None):
        types = [
            t for t in globals().values()
            if type(t) is type and issubclass(t, ModelBase)
        ] + (types or [])
        super().__init__(context=context, types=types)


@dataclass(eq=False)
class SpiceExpression(ModelBase):
    pass


@dataclass(eq=False)
class GenericExpression(ModelBase):
    braced: Any = None
    value: Any = None


@dataclass(eq=False)
class BracedExpression(ModelBase):
    sep: Any = None


@dataclass(eq=False)
class Expression(ModelBase):
    term: Any = None
    ternary: Any = None


@dataclass(eq=False)
class Ternary(ModelBase):
    op: Any = None
    sep: Any = None
    t: Any = None
    x: Any = None
    y: Any = None


@dataclass(eq=False)
class Conditional(ModelBase):
    expr: Any = None


@dataclass(eq=False)
class Or(ModelBase):
    left: Any = None
    op: Any = None
    right: Any = None
    sep: Any = None


@dataclass(eq=False)
class Xor(ModelBase):
    left: Any = None
    op: Any = None
    right: Any = None
    sep: Any = None


@dataclass(eq=False)
class And(ModelBase):
    left: Any = None
    op: Any = None
    right: Any = None
    sep: Any = None


@dataclass(eq=False)
class Not(ModelBase):
    op: Any = None
    operator: Any = None


@dataclass(eq=False)
class Relational(ModelBase):
    factor: Any = None
    left: Any = None
    op: Any = None
    right: Any = None
    sep: Any = None


@dataclass(eq=False)
class ConditionalFactor(ModelBase):
    boolean: Any = None
    expr: Any = None
    sep: Any = None


@dataclass(eq=False)
class Term(ModelBase):
    pass


@dataclass(eq=False)
class AddSub(ModelBase):
    left: Any = None
    op: Any = None
    right: Any = None
    sep: Any = None


@dataclass(eq=False)
class ProdDivMod(ModelBase):
    left: Any = None
    op: Any = None
    right: Any = None
    sep: Any = None


@dataclass(eq=False)
class Sign(ModelBase):
    op: Any = None
    operator: Any = None


@dataclass(eq=False)
class Exponential(ModelBase):
    left: Any = None
    op: Any = None
    right: Any = None
    sep: Any = None


@dataclass(eq=False)
class Functional(ModelBase):
    pass


@dataclass(eq=False)
class Variable(ModelBase):
    factor: Any = None
    sep: Any = None
    variable: Any = None


@dataclass(eq=False)
class Factor(ModelBase):
    sep: Any = None


@dataclass(eq=False)
class Functions(ModelBase):
    pass


@dataclass(eq=False)
class Value(ModelBase):
    imag: Any = None
    real: Any = None
    unit: Any = None


@dataclass(eq=False)
class ImagValue(ModelBase):
    value: Any = None


@dataclass(eq=False)
class RealValue(ModelBase):
    value: Any = None


@dataclass(eq=False)
class NumberScale(ModelBase):
    scale: Any = None
    value: Any = None


@dataclass(eq=False)
class Unit(ModelBase):
    pass


@dataclass(eq=False)
class Hz(ModelBase):
    pass


@dataclass(eq=False)
class Float(ModelBase):
    pass


@dataclass(eq=False)
class Int(ModelBase):
    pass


@dataclass(eq=False)
class BinaryPattern(ModelBase):
    pattern: Any = None


@dataclass(eq=False)
class Device(ModelBase):
    pass


@dataclass(eq=False)
class NetNode(ModelBase):
    node: Any = None
    sep: Any = None


@dataclass(eq=False)
class Separator(ModelBase):
    comment: Any = None


@dataclass(eq=False)
class Comment(ModelBase):
    pass
