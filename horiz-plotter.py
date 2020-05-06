    def PlotBar(self):
        try:
            with open(self.ChromFile, "r") as f:  # figure out how much metadata there is
                pass
        except AttributeError as e:
            print
            ctypes.windll.user32.MessageBoxW(0, u"No file loaded. Load CSV to plot.", u"Bar Graph plot error", 0)
            return
        # Plot the data
        sns.set_color_codes("pastel")


        self.BarGraphCount = int(self.barGraphEntry.get())
        print(self.BarGraphCount)
        self.Data3_marketing_bar = self.Data3_marketing.head(self.BarGraphCount)
        self.Data3_marketing_barx = self.Data3_marketing_bar['Relative-%'].tolist()
        self.Data3_marketing_bary = self.Data3_marketing_bar['Compound name'].tolist()

        sns.barplot(x=self.Data3_marketing_barx, y=self.Data3_marketing_bary, palette="rocket", label=path.basename(self.ChromFile))

        # Plot the crashes where alcohol was involved
        # sns.set_color_codes("muted")
        # sns.barplot(x="percent", y="Compound", data=Data2, label="Alcohol-involved", color="g")

        # Add a legend and informative axis label
        #ax.legend(ncol=3, loc="lower right", frameon=True)
        ax.set(xlim=(0, 60), ylabel="Top 20 Compounds",
               xlabel="Relative-%")


        sns.despine(left=False, bottom=False)
        plt.tight_layout()
        plt.savefig("FIG_BA.svg", dpi=300, transparent=False)
        plt.show()
