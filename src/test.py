import tests

valid_tests = {
    "caugh_and_fever": tests.CoughAndFever,
    # "faithfulness": tests.Faithfulness,
    # "roar_faithfulness": tests.ROARFaithfulness,
    # "roar_monotonicity": tests.ROARMonotonicity,
    # "monotonicity": tests.Monotonicity,
    # "roar": tests.Roar,
    # "shapley": tests.Shapley,
    # "shapley_corr": tests.ShapleyCorr,
    # "infidelity": tests.Infidelity
}


class Test:
    def __init__(self, name, **kwargs):
        if name not in valid_tests.keys():
            raise NotImplementedError("This test is not supported at the moment.")
        self.name = name
        self.metric = lambda model, trained_model, data_class: valid_tests[name](model, trained_model, data_class, **kwargs)
        self.evaluate = valid_tests[name].evaluate