
import random
from operator import le, mod
from random import sample, shuffle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from numpy.lib.function_base import percentile
from sklearn import metrics

class ContinuousGeneticAlgorithm:
    def __init__(
        self,
        search_space_metadata: dict,
        model_class,
        X_train: list,
        y_train: list,
        X_test: list,
        y_test: list,
        max_jobs: int = 1,
    ):
        """ """
        self.search_space = dict()
        self.search_space_metadata = search_space_metadata
        for param in search_space_metadata.keys():
            self.search_space[param] = self.search_space_metadata[param]["values"]
        print(self.search_space)
        self.model_class = model_class
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
        self.max_jobs = max_jobs

        # step 1: set GA parameters
        self.population_size = 50
        self.max_number_of_iterations = 10
        self.accuracy_table = dict()
        self.individuals_metadata = dict()
        self.mutation_rate = 0.002
        self.k = 1
        self.initial_population = dict()
        self.hyperparameter_names = list(self.search_space.keys())

    def initial_population_graph(self):
        """ """
        df = pd.DataFrame(self.individuals_metadata[1])
        plt.scatter(df.iloc[:, 0], df.iloc[:, 1])
        plt.title("Initial Population Graph Using the Distance Formula")
        plt.show()

    def random_function(self):
        search_space = list(zip(*self.search_space.values()))
        random_sample = random.sample(search_space, k=len(self.individuals_metadata[1]))
        plt.scatter(*zip(*random_sample))
        plt.title("Initial Population Graph Using a Random Function")
        plt.show()

    def caclulate_distance(self, x1, y1, x2, y2):
        """ """
        distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        return distance

    def generate_initial_generation(self, first_generation):
        """ """

        # setting the ball radius
        ball_radius = 0.09

        initial_population = list()
        temp_pop = list()

        param1_key = list(self.search_space.keys())[0]
        param2_key = list(self.search_space.keys())[1]

        # shuffle and approximate the search space
        for key in self.search_space.keys():
            shuffle(self.search_space[key])

        for param1, param2 in zip(*self.search_space.values()):
            initial_population_params = dict()
            # an empty list of the initial population
            if not initial_population:
                initial_population_params[param1_key] = param1
                initial_population_params[param2_key] = param2
                temp_pop.append((param1, param2))
                initial_population.append(initial_population_params)
            else:
                if all(
                    self.caclulate_distance(param1, param2, individum[0], individum[1])
                    > ball_radius
                    for individum in temp_pop
                ):
                    temp_pop.append((param1, param2))

                    initial_population_params[param1_key] = param1
                    initial_population_params[param2_key] = param2
                    initial_population.append(initial_population_params)

        self.individuals_metadata[first_generation] = initial_population

    def calculate_fitness(self, hyperparameter_configuration, current_generation_index):
        """ """
        # create a dict for the current individual (hyperparameter configuration)
        # individual = dict(zip(list(self.search_space.keys()), tuple(hyperparameter_configuration)))
        hyp_config = tuple(hyperparameter_configuration.values())

        if hyp_config not in self.accuracy_table:
            print("fuck")
            print(self.model_class(**hyperparameter_configuration))

            model = self.model_class(**hyperparameter_configuration)
            preds_test = model.run_the_model()

            model_error = get_reconstruction_error(self.X_test, preds_test)
            # y_pred = model.predict(self.X_test)
            # model_accuracy = metrics.accuracy_score(self.y_test, y_pred)

            self.accuracy_table[hyp_config] = model_error
            print("model error", model_error)

        else:
            model_error = self.accuracy_table[hyp_config]

        individual_index = self.individuals_metadata[current_generation_index].index(
            hyperparameter_configuration
        )
        print("individual_index", individual_index)
        self.individuals_metadata[current_generation_index][individual_index][
            "accuracy"
        ] = model_error

    def caculate_selection_probability(self, current_population, fitness_sum, accum_acc):
        """ """
        selection_probabilities = list()
        accum_fitness_sum = fitness_sum - accum_acc

        for metadata in current_population:
            # creating a new tuple of hyperparams configuration without the accuracy value
            hypr_config = tuple(metadata.values())[:-1]
            hypr_config_fitness = self.accuracy_table[hypr_config]
            selection_probability = (1 / hypr_config_fitness) / accum_fitness_sum
            selection_probabilities.append(selection_probability)

        return selection_probabilities

    def roulette_wheel_selection(
        self, current_population, generation_index, total_number_of_individuals
    ):
        """ """

        selection_probabilities = list()
        generation_fitness_sum = 0
        for individual_metadata in self.individuals_metadata[generation_index]:
            generation_fitness_sum += 1 / individual_metadata["accuracy"]

        accumulative_accuracy = 0

        # select one individual based on the computed probability
        selected_individuals = list()
        while len(selected_individuals) < (total_number_of_individuals // 2):

            current_population = [
                individum
                for individum in current_population
                if individum not in selected_individuals
            ]

            selection_probabilities = self.caculate_selection_probability(
                current_population, generation_fitness_sum, accumulative_accuracy
            )

            selected_individual_index = np.random.choice(
                len(current_population), p=selection_probabilities
            )

            selected_individual = current_population[selected_individual_index]
            # add the selected individual to the selected_individuals array
            selected_individuals.append(selected_individual)

            # update the accumlative_accuracy
            accumulative_accuracy += (
                1 / self.accuracy_table[tuple(selected_individual.values())[:-1]]
            )
        for value in self.individuals_metadata[generation_index]:
            print("selection", value["accuracy"])

        return selected_individuals

    def recombination(self, selected_individuals):
        """ """
        children = list()

        while len(selected_individuals) > 1:
            print("Selected no deletion")
            print(selected_individuals)
            # choose randomly two parents for rercombination
            parent1, parent2 = random.sample(selected_individuals, 2)
            # remove the selected elements
            selected_individuals = [
                element for element in selected_individuals if element not in (parent1, parent2)
            ]
            # intial children values
            child1 = {param: value for param, value in parent1.items() if not param == "accuracy"}
            child2 = {param: value for param, value in parent2.items() if not param == "accuracy"}

            # determine the crossover point (<parent> i)
            parent1_i = random.choice(self.hyperparameter_names)
            parent2_i = random.choice(self.hyperparameter_names)

            # draw a random integer between 1 and 1000 (M)
            M = np.random.randint(1, 1001)

            # compute delta_x and delta_y
            delta_x = child1[parent1_i] / M
            delta_y = child2[parent2_i] / M

            # calculate the new cooridnates values
            child_x = child1[parent1_i] + delta_y - delta_x
            child_y = child2[parent2_i] - delta_y + delta_x

            # combine the child coordinates
            child1[parent1_i] = child_x
            child2[parent2_i] = child_y

            # append the offpsrings to the list of children
            children.append(child1)
            children.append(child2)

        return children

    def mutate(self, child):
        """ """
        # draw a random key of all current params
        i = random.choice(self.hyperparameter_names)

        # draw another integer (M) between 1 and 10
        M = np.random.randint(1, 11)

        # calculate the upper and lower bound of the parameter
        accuracy = 0.001
        half_degree_of_the_accuracy = accuracy / 2

        UpBd = round(child[i] + half_degree_of_the_accuracy, 5)
        LowBd = round(child[i] - half_degree_of_the_accuracy, 5)

        # determine the change in the component of the child
        delta_x = (UpBd - LowBd) / M

        k_delta_x = self.k * delta_x

        k_delta_x_random = np.random.choice([-k_delta_x, k_delta_x])

        child_component_mutated = child[i] + k_delta_x_random

        child[i] = child_component_mutated
        return child

    def check_constraints(self, current_generation):
        """
        check_datatype
        check_max_and_min_values
        """
        for config in current_generation:
            print(config)
            for param in config.keys():
                # check if the datatype is not float
                print(param)
                if self.search_space_metadata[param]["dtype"] == np.int64:
                    print(type(config[param]))
                    print("shit 1 happened")
                    print(param, config[param])
                    config[param] = int(config[param])
                # check if the param value doesn't exceed the max allowed
                if config[param] > self.search_space_metadata[param]["max"]:
                    print("shit 2 happened")
                    print(param, config[param])
                    config[param] = self.search_space_metadata[param]["max"]
                # check if the param value fall behind the min allowed
                if config[param] < self.search_space_metadata[param]["min"]:
                    print("shit 3 happened")
                    print(param, config[param])
                    config[param] = self.search_space_metadata[param]["min"]

        return current_generation

    def optimize(self):
        """ """

        # generate an intial population covering homogeneously the whole search space
        current_generation_index = 1
        self.generate_initial_generation(current_generation_index)

        # loop till reaching the maximum number of iteration
        while current_generation_index < self.max_number_of_iterations:
            print("Current generation", current_generation_index)
            current_generation = self.individuals_metadata[current_generation_index]
            print(current_generation)
            print("Generation: ", len(current_generation))
            total_number_of_individuals = len(current_generation)

            for individual in current_generation:
                self.calculate_fitness(individual, current_generation_index)

            # select the individuals with the best characteristics based on a probability

            selected_individuals = self.roulette_wheel_selection(
                current_generation, current_generation_index, total_number_of_individuals
            )

            # recombination of individuals

            children = self.recombination(selected_individuals)

            current_generation = list()
            for child in children:
                # draw a random number to compare it to the mutation rate
                random_number = np.random.uniform(0, 1)
                if random_number < self.mutation_rate:
                    child = self.mutate(child)
                current_generation.append(child)

            if not current_generation:
                print("Terminated")
                break
            current_generation = self.check_constraints(current_generation)
            current_generation_index += 1
            self.individuals_metadata[current_generation_index] = current_generation
        return self.individuals_metadata
