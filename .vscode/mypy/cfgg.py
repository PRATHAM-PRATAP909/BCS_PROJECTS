from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'NumPy Tutorial Cheat Sheet', 0, 1, 'C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, func_name, explanation, code, output):
        # Function Name and Explanation
        self.set_font('Arial', 'B', 10)
        self.cell(0, 5, func_name, 0, 1)
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 5, explanation)
        self.ln(2)
        
        # Code Block
        self.set_font('Courier', '', 9)
        self.set_fill_color(240, 240, 240)
        self.multi_cell(0, 5, code, 0, 'L', True)
        
        # Output Block
        self.set_font('Courier', 'I', 9)
        self.cell(0, 5, f"# Output: {output}", 0, 1)
        self.ln(5)

pdf = PDF()
pdf.add_page()

# --- Content Data ---
content = {
    "I. NumPy Tutorial (Core Basics)": [
        ("np.array()", "Creates an array from a list or tuple.", "arr = np.array([1, 2, 3])\nprint(arr)", "[1 2 3]"),
        ("Indexing []", "Accesses a specific element by its position.", "arr = np.array([10, 20, 30])\nprint(arr[1])", "20"),
        ("Slicing [:]", "Extracts a portion of the array from start to end index.", "arr = np.array([1, 2, 3, 4, 5])\nprint(arr[1:4])", "[2 3 4]"),
        ("dtype", "Attribute to check the data type of the array elements.", "arr = np.array([1, 2, 3])\nprint(arr.dtype)", "int64"),
        ("astype()", "Converts the array to a different data type.", "arr = np.array([1.1, 2.9])\nprint(arr.astype('i'))", "[1 2]"),
        ("copy()", "Creates a completely new array; changes do not affect original.", "arr = np.array([1, 2, 3])\nx = arr.copy()\nx[0] = 9\nprint(arr)", "[1 2 3]"),
        ("view()", "Creates a view of the original array; changes affect original.", "arr = np.array([1, 2, 3])\nx = arr.view()\nx[0] = 9\nprint(arr)", "[9 2 3]"),
        ("shape", "Attribute that returns a tuple representing array dimensions.", "arr = np.array([[1, 2], [3, 4]])\nprint(arr.shape)", "(2, 2)"),
        ("reshape()", "Changes the shape of an array without changing its data.", "arr = np.array([1, 2, 3, 4])\nprint(arr.reshape(2, 2))", "[[1 2] [3 4]]"),
        ("nditer()", "Efficient multi-dimensional iterator object.", "arr = np.array([[1, 2], [3, 4]])\nfor x in np.nditer(arr): pass", "1 2 3 4 (iterated)"),
        ("concatenate()", "Joins a sequence of arrays along an existing axis.", "arr1 = np.array([1, 2])\narr2 = np.array([3, 4])\nprint(np.concatenate((arr1, arr2)))", "[1 2 3 4]"),
        ("stack()", "Joins a sequence of arrays along a new axis.", "print(np.stack((arr1, arr2), axis=1))", "[[1 3] [2 4]]"),
        ("array_split()", "Splits an array into multiple sub-arrays.", "arr = np.array([1, 2, 3, 4, 5, 6])\nprint(np.array_split(arr, 3))", "[arr([1, 2]), arr([3, 4])...]"),
        ("where()", "Returns indices of elements that satisfy a condition.", "arr = np.array([1, 2, 3, 4, 5])\nprint(np.where(arr == 4))", "(array([3]),)"),
        ("sort()", "Returns a sorted copy of an array.", "arr = np.array([3, 2, 0, 1])\nprint(np.sort(arr))", "[0 1 2 3]"),
        ("Boolean Indexing", "Filtering elements based on a condition.", "arr = np.array([41, 42, 43, 44])\nprint(arr[arr > 42])", "[43 44]")
    ],
    "II. NumPy Random": [
        ("rand()", "Generates random float numbers between 0 and 1.", "from numpy import random\nprint(random.rand())", "0.1234..."),
        ("randint()", "Generates a random integer.", "print(random.randint(100))", "42 (random 0-100)"),
        ("shuffle()", "Modifies a sequence in-place by shuffling its contents.", "arr = np.array([1, 2, 3, 4, 5])\nrandom.shuffle(arr)\nprint(arr)", "[3 1 5 2 4]"),
        ("permutation()", "Randomly permutes a sequence or returns a permuted range.", "print(random.permutation([1, 2, 3]))", "[2 1 3]"),
        ("normal()", "Draws random samples from a normal (Gaussian) distribution.", "x = random.normal(loc=1, scale=2, size=(2, 2))\nprint(x)", "[[1.2 -0.5] [2.1 0.8]]"),
        ("binomial()", "Draws samples from a binomial distribution.", "x = random.binomial(n=10, p=0.5, size=5)\nprint(x)", "[5 4 6 5 5]"),
        ("poisson()", "Draws samples from a Poisson distribution.", "x = random.poisson(lam=2, size=5)\nprint(x)", "[2 1 3 2 0]"),
        ("uniform()", "Draws samples from a uniform distribution.", "x = random.uniform(size=(2, 2))\nprint(x)", "[[0.1 0.9] [0.4 0.2]]")
    ],
    "III. NumPy ufunc": [
        ("frompyfunc()", "Converts a Python function to a NumPy ufunc.", "def my_add(x, y): return x+y\nmy_ufunc = np.frompyfunc(my_add, 2, 1)\nprint(my_ufunc([1], [2]))", "[3]"),
        ("add()", "Adds arguments element-wise.", "print(np.add([10, 20], [30, 40]))", "[40 60]"),
        ("trunc()", "Removes decimals, returning float closest to zero.", "print(np.trunc([-3.1666, 3.6667]))", "[-3.  3.]"),
        ("log2()", "Base-2 logarithm.", "print(np.log2([1, 4, 8]))", "[0. 2. 3.]"),
        ("sum()", "Sum of array elements over a given axis.", "print(np.sum([[1, 2], [3, 4]]))", "10"),
        ("prod()", "Product of array elements over a given axis.", "print(np.prod([1, 2, 3]))", "6"),
        ("diff()", "Calculates the discrete difference between elements.", "arr = np.array([10, 15, 25])\nprint(np.diff(arr))", "[5 10]"),
        ("lcm()", "Returns the Lowest Common Multiple.", "print(np.lcm(4, 6))", "12"),
        ("gcd()", "Returns the Greatest Common Divisor.", "print(np.gcd(6, 9))", "3"),
        ("sin()", "Trigonometric sine (input in radians).", "print(np.sin(np.pi/2))", "1.0"),
        ("unique()", "Returns sorted unique elements of an array.", "arr = np.array([1, 1, 2, 3])\nprint(np.unique(arr))", "[1 2 3]")
    ]
}

# --- Generate PDF ---
for section, items in content.items():
    pdf.chapter_title(section)
    for func, expl, code, out in items:
        pdf.chapter_body(func, expl, code, out)

pdf.output("NumPy_Tutorial_Cheat_Sheet.pdf")