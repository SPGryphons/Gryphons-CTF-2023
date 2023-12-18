from z3 import And, Bool, Not, Or, Solver, solve, Xor, simplify, sat, BoolRef, Bool
import json
def Nand(a, b):
    return Not(And(a, b))

def Nor(a, b):
    return Not(Or(a, b))


with open("diagram.json", "r") as f:
    f_contents = f.read()
    f_json = json.loads(f_contents)




# Store the gates by the output, not the input.
gates = {}

def add_to_gate(key, entry):
    if key in gates:
        gates[key].append(entry)
    else:
        gates[key] = [entry]



# 1 NAND should have 2 inputs. (give as hint)
#    [ "sr1:Q7", "nand16:A", "green", [ "v0" ] ], // input, output, don't need to care
# this is the connections only.
# we add the gates first.

accepted_types = ["wokwi-gate-nand-2", "wokwi-gate-or-2", "wokwi-gate-xor-2", "wokwi-gate-not", "wokwi-gate-and-2" ]

for part in f_json["parts"]:
    if part["type"] in accepted_types:
        gates[Bool(part["id"])] = []


sources = ["Q7", "Q6", "Q5", "Q4", "Q3", "Q2", "Q1", "Q0"]
start_alt = ['flop1', 'flop2', 'flop3', 'flop4', 'flop5', 'flop6', 'flop7', 'flop8', "flop9","flop10","flop11","flop12","flop13","flop14","flop15","flop16"]
for source in sources:
    gates[Bool(source)] = []
for source in start_alt:
    gates[Bool(source)] = []


start_types = ["OUT", *sources, "GND", "VCC"]
source_types = ["sr1", "gnd", *start_alt]
end_types = ["IN", "A", "B"]

for connection in f_json["connections"]:
    # Connections may be swapped.
    # OUT is for start of the connection
    # IN(NOT only), A, B is for end of the connection
    # sr1: is start of the connection
    # We store stuff using the end of the connection with ID only, not A or B.
    end_1 = connection[0]
    end_2 = connection[1]

    # check end_1
    tmp = end_1.split(":")
    print("tmp", tmp)
    start = -1j
    if tmp[1] in start_types or tmp[0] in source_types:
        start = end_1
    elif tmp[1] in end_types:
        end = end_1
    else:
        print("Part not recognised", end_1, end_2, tmp[1])
        continue
    print("tmp", tmp)

    tmp = end_2.split(":")
    if tmp[1] in start_types or tmp[0] in source_types:
        if start != -1j:
            print("DOUBLE START! SKIPPING!")
            continue
        start = end_2
    elif tmp[1] in end_types:
        end = end_2
    else:
        print("Part not recognised", end_1, end_2)
        continue

    # If no such gate, we delibrately raise an exception
    start_split = start.split(":")
    print("start split", start_split, start_split[0] in start_alt)
    if start_split[0] in start_alt:
        start_id = start_split[0]
    elif start_split[0] in source_types:
        start_id = start_split[1]
    else:
        start_id = start_split[0]

    end_id = end.split(":")[0]

    gates[Bool(end_id)].append(Bool(start_id))






print("Gates formed is", gates)
source = [Bool("Q7"), Bool("Q6"), Bool("Q5"), Bool("Q4"), Bool("Q3"), Bool("Q2"), Bool("Q1"), Bool("Q0"), Bool("flop1"), Bool("flop2"), Bool("flop3"), Bool("flop4"), Bool("flop5"), Bool("flop6"), Bool("flop7"), Bool("flop8"),Bool("flop9"),Bool("flop10"),Bool("flop11"),Bool("flop12"),Bool("flop13"),Bool("flop14"),Bool("flop15"),Bool("flop16")]
# Which NAND is the output?
# in this case its NAND13.
def trace(gate):
    if gate in source:
        print("BASE CASE", gate)
        return gate # Base case, which is the inputs itself.
    strgate = str(gate)
    if strgate.startswith("gnd"):
        return False
    elif strgate.startswith("vcc"):
        return True


    connected = gates[gate]
    print("CONNECTED", gate, connected, len(connected))
    if len(connected) == 0:
        print("NO ITEMS IN LIST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    if strgate.startswith("nand"):
        return Nand(trace(connected[0]), trace(connected[1]))
    elif strgate.startswith("or"):
        return Or(trace(connected[0]), trace(connected[1]))
    elif strgate.startswith("not"):
        return Not(trace(connected[0]))
    elif strgate.startswith("xor"):
        return Xor(trace(connected[0]), trace(connected[1]))
    elif strgate.startswith("and"):
        return And(trace(connected[0]), trace(connected[1]))
    else:
        raise Exception(f"Not implemented: {gate}")


a = trace(Bool("xor1"))
print(a)
print("simplification", simplify(a))
solver = Solver()
solver.add(a == True)
if solver.check() == sat:
    print("RESULT")
    model = solver.model()
    print(model, type(model), dir(model), model.model)
    sorted_model = sorted ([(x, model[x]) for x in model], key = lambda x: str(x[0]))
    print(sorted_model)

else:
    print("Unsatisfiable")


