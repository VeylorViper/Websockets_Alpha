import h5py
import matplotlib.pyplot as plt

def LoadH5(file_path, dataset_name):
    try:
        with h5py.File(file_path, 'r') as file:
            # Check if the dataset exists
            if dataset_name not in file:
                raise KeyError(f"Dataset '{dataset_name}' not found in the HDF5 file.")

            # Read the dataset into a NumPy array
            dataset = file[dataset_name][...]
            return dataset
    except Exception as e:
        print(f"Error reading HDF5 dataset: {str(e)}")
        return None
    
A = LoadH5("TestData4.h5",'1')
# print(len(A))
    
def SalesOverview(Activity,OverviewDuration):
    Length = len(Activity)
    _Overview_Activity = []
    for j in range(0,Length-OverviewDuration):
        Summed = sum(Activity[j:j+OverviewDuration])
        _Overview_Activity.append(Summed)
    return _Overview_Activity

Neutral = [(i*0) for i, _ in enumerate(A)]

print("Total Buy Power : ",sum([i for i,_ in enumerate(A) if _ > 0]))
print("Total Sell Power : ",sum([i for i,_ in enumerate(A) if _ < 0]))
print("Difference : ",abs((sum([i for i,_ in enumerate(A) if _ > 0])) - (sum([i for i,_ in enumerate(A) if _ < 0])))) 
plt.plot(A)
plt.plot(Neutral)
plt.savefig("Activity4.png")

plt.figure()
plt.plot(SalesOverview(A,500))
plt.plot(Neutral)
plt.show()