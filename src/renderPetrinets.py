import os

from pm4py.objects.petri_net.obj import (PetriNet, Marking)
from pm4py.objects.petri_net.utils import petri_utils
from pm4py.visualization.petri_net import visualizer as pn_visualizer

# Petri-Net
net = PetriNet("BspPetriNet")

# Transitions
t_0 = PetriNet.Transition("t_0", "Diagnose")
t_1 = PetriNet.Transition("t_1", "Weiterbehandlung")
t_2 = PetriNet.Transition("t_2","Laboruntersuchung")
t_3 = PetriNet.Transition("t_3","Pflegen")
t_4 = PetriNet.Transition("t_4", "Visite")
t_5 = PetriNet.Transition("t_5", "Medikamente")
t_6 = PetriNet.Transition("t_6","Entlassung")

net.transitions.add(t_0)
net.transitions.add(t_1)
net.transitions.add(t_2)
net.transitions.add(t_3)
net.transitions.add(t_4)
net.transitions.add(t_5)
net.transitions.add(t_6)

# Places
p_start = PetriNet.Place("p_start")
p_end = PetriNet.Place("p_end")
p_1 = PetriNet.Place("p_1")
p_2_a = PetriNet.Place("p_2_a")
p_2_b = PetriNet.Place("p_2_b")
p_2_c = PetriNet.Place("p_2_c")
p_2_d = PetriNet.Place("p_2_d")
p_3_a = PetriNet.Place("p_3_a")
p_3_b = PetriNet.Place("p_3_b")
p_3_c = PetriNet.Place("p_3_c")
p_3_d = PetriNet.Place("p_3_d")

net.places.add(p_start)
net.places.add(p_end)
net.places.add(p_1)
net.places.add(p_2_a)
net.places.add(p_2_b)
net.places.add(p_2_c)
net.places.add(p_2_d)
net.places.add(p_3_a)
net.places.add(p_3_b)
net.places.add(p_3_c)
net.places.add(p_3_d)

# Kanten
petri_utils.add_arc_from_to(p_start, t_0, net)

petri_utils.add_arc_from_to(t_0, p_1, net)
petri_utils.add_arc_from_to(p_1, t_1, net)
petri_utils.add_arc_from_to(p_1, t_6, net)

petri_utils.add_arc_from_to(t_1, p_2_a, net)
petri_utils.add_arc_from_to(t_1, p_2_b, net)
petri_utils.add_arc_from_to(t_1, p_2_c, net)
petri_utils.add_arc_from_to(t_1, p_2_d, net)
petri_utils.add_arc_from_to(p_2_a, t_2, net)
petri_utils.add_arc_from_to(p_2_b, t_3, net)
petri_utils.add_arc_from_to(p_2_c, t_4, net)
petri_utils.add_arc_from_to(p_2_d, t_5, net)

petri_utils.add_arc_from_to(t_2, p_3_a, net)
petri_utils.add_arc_from_to(t_3, p_3_b, net)
petri_utils.add_arc_from_to(t_4, p_3_c, net)
petri_utils.add_arc_from_to(t_5, p_3_d, net)
petri_utils.add_arc_from_to(p_3_a, t_0, net)
petri_utils.add_arc_from_to(p_3_b, t_0, net)
petri_utils.add_arc_from_to(p_3_c, t_0, net)
petri_utils.add_arc_from_to(p_3_d, t_0, net)

petri_utils.add_arc_from_to(t_6, p_end, net)

# markings
initial_marking = Marking()
initial_marking[p_start] = 1

final_marking = Marking()
final_marking[p_end] = 1

parameters_pdf = { "format": "pdf",
                   "graph_attr": { "rankdir": "LR",
                                   "splines": "ortho",
                                   "nodesep": "0.6",
                                   "ranksep": "1.0",
                                   "bgcolor": "white"
                                   },
                   "node_attr": { "fontname": "Helvetica",
                                  "fontsize": "12"
                                  },
                   "edge_attr": { "fontname": "Helvetica",
                                  "fontsize": "10",
                                  "arrowsize": "0.7"
                                  }
                   }

parameters_svg = {
    "format": "svg",
    "graph_attr": {
        "rankdir": "LR",
        "splines": "ortho",
        "nodesep": "0.6",
        "ranksep": "1.2"
    }
}

gviz_svg = pn_visualizer.apply(net, initial_marking, final_marking, parameters= parameters_svg)
qviz_pdf = pn_visualizer.apply(net, initial_marking, final_marking, parameters= parameters_pdf)


path = r"C:\Users\valen\PycharmProjects\graphviz_BA\output"
os.makedirs(path, exist_ok=True)
pn_visualizer.save(gviz_svg, os.path.join(path, "petri_net.svg"))
pn_visualizer.save(qviz_pdf, os.path.join(path, "petri_net.pdf"))