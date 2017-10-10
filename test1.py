class SetOfParliamentMembers:


    #[...]


    def display_chart(self):

        data = self.dataframe

        female_mps = data[data.sexe == "F"]

        male_mps = data[data.sexe == "H"]


        counts = [len(female_mps), len(male_mps)]

        counts = np.array(counts)

        nb_mps = counts.sum()

        proportions = counts / nb_mps


        labels = ["Female ({})".format(counts[0]), "Male ({})".format(counts[1])]


        fig, ax = plt.subplots()

        ax.axis("equal")

        ax.pie(

                proportions,

                labels=labels,

                autopct="%1.1f pourcents"

                )

        plt.title("{} ({} MPs)".format(self.name, nb_mps))

        plt.show()