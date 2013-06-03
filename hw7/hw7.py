from Orange import orange


def train(data):
    bayes = orange.BayesLearner(data)
    return bayes


def test_train(data, bayes):
    classes = list(data.domain.classVar.values)
    correct = 0.0
    for example in data:
        clid = classes.index(example.getclass())
        p = list(apply(bayes, [example, orange.GetProbabilities]))
        if clid == p.index(max(p)):
            correct += 1

    print "Possible classes:", classes
    print correct/len(data)


def test(data, bayes):
    ans = ['CEU', 'GIH', 'JPT', 'ASW', 'YRI']
    for example in data:
        classifier = bayes(example)
        print ans.index(classifier),

if __name__ == '__main__':
    #Load Data
    train_data = orange.ExampleTable("genestrain.tab")
    test_data = orange.ExampleTable("genesblind.tab")

    #Train
    #bayes = train(train_data.get_items(range(10)))
    bayes = train(train_data)
    #Test
    test(test_data, bayes)
