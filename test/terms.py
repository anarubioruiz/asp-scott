from clorm import ComplexTerm, Predicate, ConstantField, IntegerField


class Act(Predicate):
    id = ConstantField

class FeatureOfInterest(Predicate):
    id = ConstantField

class Sensor(Predicate):
    id = ConstantField

class ObservableProperty(Predicate):
    id = ConstantField

class Observation(Predicate):
    id = ConstantField

class Actuator(Predicate):
    id = ConstantField

class Actuation(Predicate):
    id = ConstantField

class ActuatableProperty(Predicate):
    id = ConstantField

class Result(Predicate):
    id = ConstantField

class Platform(Predicate):
    id = ConstantField

class isObservedBy(Predicate):
    observable_property = ConstantField
    sensor = ConstantField

class observes(Predicate):
    sensor = ConstantField
    observable_property = ConstantField

class makesObservation(Predicate):
    sensor = ConstantField
    observation = ConstantField

class madeBySensor(Predicate):
    observation = ConstantField
    sensor = ConstantField

class observedProperty(Predicate):
    observation = ConstantField
    observable_property = ConstantField

class makesActuation(Predicate):
    actuator = ConstantField
    actuation = ConstantField

class isActedOnBy(Predicate):
    actuatable_property = ConstantField
    actuator = ConstantField

class madeByActuator(Predicate):
    actuation = ConstantField
    actuator = ConstantField

class actsOnProperty(Predicate):
    actuator = ConstantField
    actuatable_property = ConstantField

class hasFeatureOfInterest(Predicate):
    act = ConstantField
    feature_of_interest = ConstantField

class isFeatureOfInterestOf(Predicate):
    feature_of_interest = ConstantField
    act = ConstantField

class isResultOf(Predicate):
    result = ConstantField
    act = ConstantField

class hasResult(Predicate):
    act = ConstantField
    result = ConstantField

class hasSimpleResult(Predicate):
    act = ConstantField
    result = ConstantField

class hosts(Predicate):
    platform = ConstantField
    hosted = ConstantField

class isHostedBy(Predicate):
    hosted = ConstantField
    platform = ConstantField
