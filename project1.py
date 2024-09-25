import ollama
import sys

#takes in a text file, 
def open_prompts(txt):
    promptsFile = open(txt,"r")
    prompts = []
    for line in promptsFile:
        line = line.rstrip('\n')
        prompts.append(line)
    promptsFile.close()
    return prompts
#Writes to a txt, takes an array and the name of a text file
def write_responses(responses,txt):
    n = 1
    results_file = open(txt,"w")
    for line in responses:
        results_file.write(f'Response {n}.\n{line}\n\n')
        n+=1
    results_file.close()
#gives a prompt to phi3-mini and returns the response
def get_response(prompt):
    resp = ollama.generate(model="phi3:mini",prompt=prompt)
    return (resp["response"])

#Takes two arguments, name of prompts text file, name of output textfile
if __name__ == "__main__":
    prompts = open_prompts(sys.argv[1])
    results = []
    for element in prompts:
        results.append(get_response(element))
    write_responses(results,sys.argv[2])
    print(f'Worked so far! :D')