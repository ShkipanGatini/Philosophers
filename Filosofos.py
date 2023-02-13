while True:
    userPrompt= input("Which philosopher are we seeing today?")
    prefixes= ["Dec","dec","Des","Dec"]
    if userPrompt.startswith(tuple(prefixes)):
        print("Descartes: Philosopher born in Europe, his position was against Medievalist philosophy" "\n"
        "He started doubting his own thoughts, and as such, they wouldn't be able to provide a proper view on reality" "\n"
        "Thus, what could provide his own thoughts with certainty? His own reasoning, since he could think, he could think of the being of thoughts""\n"
        "He could doubt anything, but one thing he couldn't doubt was his own reasoning, if he could think, he could exist, cogito ergo sum." )
    prefixes2=["Realism","Jurdical realism","realism","Juridical realism"]
    if userPrompt.startswith(tuple(prefixes2)):
        print("Juridical realism: Unlike positivism and Natural law school, Juridical Realism believes that law is what we can find in the physical world " "\n"
        "Juridical Realism deems both previous theories as ideologies, since they try to shoehorn actual facts under their view" "\n"
        " *American Realism: Holmes/Cohen/Frank/Cardozo They believe that law is what lawyers do, in order to understand law, we should look at what lawyers do and think from the point of view of a  theoretical bad man" "\n"
        "*They think in terms of facts, not words" "\n"
        "Cardozo:Law never is, it is always about to materialize ""\n"
        "Cohen:law are those norms on which judges decide cases" "\n"
        "Frank: Usually the judges arrive to a conclusion and go backwards in terms of their opinion, not vice-versa" "\n" 
        "Gray: Law is the application of the sources of law by the judges")
    prefixes3=["Scandinavian","scandinavian"]
    if userPrompt.startswith(tuple(prefixes3)):
        print("Scandinavian realism represented by Olivercrona and Hagerstrom, it believes that trying to discover law is akin to finding God:There is only a pscyhological connection" "\n"
        "Between the obligatoriness of law and the minds of the common people, objectiveness will never be achieved, since law is a subjective matter")
    prefixes3=["Sociology of law,", "sociology"]
    if userPrompt.startswith(tuple(prefixes3)):
        print("Durkheim and Gurevitch: They both think in general terms of law as a self-regulatory mechanism inside a particular society, for example, the notion of public order in the Argentine Penal Code")
        