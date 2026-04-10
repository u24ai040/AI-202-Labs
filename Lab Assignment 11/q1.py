graph = {
    "Kutch": ["Banaskantha", "Surendranagar", "Rajkot","Patan"],
    "Banaskantha": ["Kutch", "Patan", "Sabarkantha", "Mehsana"],
    "Patan": ["Banaskantha", "Mehsana", "Surendranagar","Kutch"],
    "Mehsana": ["Patan", "Banaskantha", "Sabarkantha", "Gandhinagar", "Ahmedabad"],
    "Sabarkantha": ["Banaskantha", "Mehsana", "Gandhinagar", "Panchmahal","Kheda"],
    "Gandhinagar": ["Mehsana", "Sabarkantha", "Ahmedabad", "Kheda"],
    "Ahmedabad": ["Mehsana", "Gandhinagar", "Kheda", "Anand", "Surendranagar","Bhavnagar"],
    "Kheda": ["Gandhinagar", "Ahmedabad", "Anand", "Panchmahal","Sabarkantha","Vadodara"],
    "Panchmahal": ["Sabarkantha", "Kheda", "Dahod", "Vadodara"],
    "Dahod": ["Panchmahal","Vadodara"],
    "Surendranagar": ["Kutch", "Patan", "Ahmedabad", "Rajkot", "Bhavnagar"],
    "Rajkot": ["Surendranagar", "Jamnagar", "Junagadh", "Amreli","Bhavnagar","Porbandar"],
    "Jamnagar": [ "Rajkot", "Porbandar"],
    "Porbandar": ["Jamnagar", "Junagadh","Rajkot"],
    "Junagadh": ["Rajkot", "Porbandar", "Amreli"],
    "Amreli": ["Junagadh", "Rajkot", "Bhavnagar"],
    "Bhavnagar": ["Amreli", "Surendranagar","Rajkot","Ahmedabad"],
    "Anand": ["Ahmedabad", "Kheda", "Vadodara"],
    "Vadodara": ["Anand", "Panchmahal", "Bharuch", "Narmada","Dahod","Kheda"],
    "Bharuch": ["Vadodara", "Narmada", "Surat"],
    "Narmada": ["Bharuch", "Vadodara", "Surat"],
    "Surat": ["Bharuch", "Narmada", "Navsari","Dang"],
    "Navsari": ["Surat", "Valsad", "Dang"],
    "Valsad": ["Navsari"],
    "Dang": ["Navsari", "Surat"]
}

all_colors=['R','G','B','Y','B']

def solve(assign,n,domains):
  if n==len(graph):
    return True
  
  for i in graph:
    if i not in assign:

      for j in domains:
        issafe=True
        for c in graph[i]:
          if c in assign and assign[c]==j:
            issafe=False
            break
        if issafe:
          assign[i]=j
          if solve(assign,n+1,domains):
            return True
        
          del assign[i]
      return False

        
def main():

    for num_colors in range(0, 6):

        domains = all_colors[:num_colors]

        print(f"\nTrying with {num_colors} colors -> {domains}")

        assign = {}

        if solve(assign, 0, domains):
            print("\nSolution Found:")
            for state in assign:
                print(state, "->", assign[state])
            return

        else:
            print("No solution possible with", num_colors, "colors")


main()