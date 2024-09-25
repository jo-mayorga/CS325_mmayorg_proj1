import ollama
import sys
#takes in a text file, strips each line of \n before addding to array, once done reading close and return array
def open_prompts(txt):
    promptsFile = open(txt,"r")
    prompts = []
    for line in promptsFile:
        line = line.rstrip('\n')
        prompts.append(line)
    promptsFile.close()
    return prompts
#Opens a txt file, writes the information of responses to the text file, then closes.
def write_responses(responses,txt):
    n = 1
    results_file = open(txt,"w")
    for line in responses:
        results_file.write(f'Response {n}.\n{line}\n\n')
        n+=1
    results_file.close()
#gives a prompt to phi3-mini and returns the response.
def get_response(prompt):
    resp = ollama.generate(model="phi3:mini",prompt=prompt)
    return (resp["response"])
#takes two arguments, name of prompts text file, name of output textfile
if __name__ == "__main__":
    #open text file supplied in arg1 and put info from that file into prompts
    print(f'Reading from {sys.argv[1]}...\n')
    prompts = open_prompts(sys.argv[1])
    #feed each prompt to the model and store in results
    print(f'Feeding prompts from {sys.argv[1]} to phi3:mini...\n')
    results = []
    for element in prompts:
        results.append(get_response(element))
    #write the responses stored in results to text file
    print(f'Writing results to {sys.argv[2]}...\n')
    write_responses(results,sys.argv[2])
    print('Done!\n')
