using System;
using System.Collections.Generic;
using System.Linq;

namespace PythonForCSharpers
{
    class Program
    {
        public static List<Dictionary<string, string>> employees = new List<Dictionary<string, string>>
        {
            new Dictionary<string, string>
            {
                { "Position", "Manager" },
                { "Name", "James" },
                { "Department", "Finance" },
                { "City", "Philadelphia" },
                { "State", "PA" }
            },
            new Dictionary<string, string>
            {
                { "Position", "Accountant" },
                { "Name", "George" },
                { "Department", "Finance" },
                { "City", "Buffalo" },
                { "State", "NY" }
            },
            new Dictionary<string, string>
            {
                { "Position", "Guard" },
                { "Name", "Henrietta" },
                { "Department", "Operations" },
                { "City", "King of Prussia" },
                { "State", "PA" }
            },
            new Dictionary<string, string>
            {
                { "Position", "President" },
                { "Name", "Phillip" },
                { "Department", "Leadership" },
                { "City", "Cherry Hill" },
                { "State", "NJ" }
            }
        };

        public static Dictionary<string, List<Dictionary<string, string>>> pets= new Dictionary<string, List<Dictionary<string, string>>>
            {
                {
                    "dogs",
                    new List<Dictionary<string, string>>() {
                        new Dictionary<string, string>
                        {
                            { "Name", "James" },
                            { "Breed", "Bulldog" },
                            { "Color", "Brown" }
                        },
                        new Dictionary<string, string>
                        {
                            { "Name", "George" },
                            { "Breed", "Greyhound" },
                            { "Color", "Brindle" }
                        }
                    }
                },
                {
                    "cats",
                    new List<Dictionary<string, string>>() {
                        new Dictionary<string, string>
                        {
                            { "Name", "Henry" },
                            { "Breed", "Shorthair" },
                            { "Color", "White" }
                        },
                        new Dictionary<string, string>
                        {
                            { "Name", "Phillip" },
                            { "Breed", "Siamese" },
                            { "Color", "Gray" }
                        }
                    }
                }
            };

        static void Test1()
        {
            Console.WriteLine("Test 1 - iterate list");

            List<string> myList1 = new List<string> { "a", "b", "c" };
            foreach (var myItem in myList1)
            {
                Console.WriteLine($"Item: {myItem}");
            }

            var myList2 = "oops";
            foreach (var myItem in myList2)
            {
                Console.WriteLine($"Item: {myItem}");
            }
        }

        static void Test2()
        {
            Console.WriteLine("Test 2");

            foreach (KeyValuePair<string, List<Dictionary<string, string>>> item in pets)
            {
                Console.WriteLine($"Breed: {item.Key}");
                foreach (Dictionary<string, string> animal in item.Value)
                {
                    Console.WriteLine($"  Name: {animal["Name"]}");
                    Console.WriteLine($"  Breed: {animal["Breed"]}");
                    Console.WriteLine($"  Color: {animal["Color"]}");
                    Console.WriteLine($"");
                }
            }
        }

        static void Test3()
        {
            Console.WriteLine("Test 3 - filter, map, and sort");

            Console.WriteLine("Employees in PA:");
            var matches = employees
                .Where(x => x["State"] == "PA")
                .OrderBy(x => x["Name"])
                .Select(x => new { Name = x["Name"], Position= x["Position"] });
            foreach(var employee in matches)
            {
                Console.WriteLine($"{employee.Name}: {employee.Position}");
            }
        }

        static void Test4()
        {
            Console.WriteLine("Test 4 - conditional operator");

            var items = new List<string> { "a", "b", "c" };
            string message = items.Count + " " + (items.Count == 1 ? "item" : "items");
            Console.WriteLine($"The list {String.Join(',', items)} contains {message}");

            items = new List<string> { "a" };
            message = items.Count + " " + (items.Count == 1 ? "item" : "items");
            Console.WriteLine($"The list {String.Join(',', items)} contains {message}");
        }

        static void Test5()
        {
            Console.WriteLine("Test 5");

            var x = 1;
            if(x == 1)
            {
                var y = 2;
            }
            else
            {
                var z = 3;
            }
            // COMPILE TIME ERROR:
            // Console.WriteLine(y);
            // COMPILE TIME ERROR:
            // Console.WriteLine(z);
        }

        static void Test6()
        {
            Console.WriteLine("Test 6");

            string str = "When I am outside a function "
                + "I have to manually concatenate strings "
                + "and use backslash line continuation";
            Console.WriteLine(str);

            // COMPILE TIME ERROR - this doesn't work
            // Console.WriteLine("When I am inside a function "
            //    "it will automatically concatenate strings without "
            //    "a line continuation mark ");
        }


        static void Test7()
        {
            Console.WriteLine("Test 7");

            int a = 1;
            int b = a - a;
            int c = 0;
            try
            {
                c = a / b;
            }
            catch (/*DivideByZero*/Exception ex)
            {
                Console.WriteLine($"error: {ex}");
            }
            finally
            {
                Console.WriteLine($"finally, c={c}");
            }
        }

        /// <summary>
        /// Return all items in list joined by supplied separator.
        /// 
        /// Return empty string if list is null or empty.
        /// </summary>
        /// <param name="myList">List to concatenate</param>
        /// <param name="separator">Separator to use, defaults to comma</param>
        /// <returns>Joined list</returns>
        public static string MyJoinFunction(List<string> myList, string separator = ",")
        {
            string result = "";
            if(myList != null && myList.Count() > 0)
            {
                foreach(var item in myList)
                {
                    result += $"{item}{separator}";
                }
                // Remove final separator
                result = result.Substring(0, result.Length - 1);
            }
            return result;
        }

        static void Test8()
        {
            Console.WriteLine("Test 8");
            Console.WriteLine(MyJoinFunction(new List<string> { "a", "b", "c" }, ";"));
        }

        static void Test9()
        {
            Console.WriteLine("Test 9");

            // Behaves like a set, but recent addition to C# and not commonly used
            HashSet<string> mySet = new HashSet<string> { "a", "b", "c" };

            // Array
            int[] myArray = { 1, 2, 3 };

            // List
            List<string> myList = new List<string> { "a", "b", "c" };

            // Dictionary
            Dictionary<string, string> myDict = new Dictionary<string, string>
            {
                { "a", "1" },
                { "b", "3" },
                { "c", "3" }
            };

            // Tuple
            Tuple<string, string, string> myTuple = new Tuple<string, string, string>("a", "b", "c");
        }

        static void Test10()
        {
            Console.WriteLine("Test 10");

            // Simple string
            Console.WriteLine("Simple string - The quick brown fox");

            // Preserve escape characters
            Console.WriteLine(@"Preserve escape char literals - \tTab and newline\n");

            // Expand variables
            string adjective = "quick";
            string noun = "fox";
            Console.WriteLine($"Expand variables - The {adjective} brown {noun}");

            // Preserve embedded newlines
            Console.WriteLine(@"Preserve embedded newlines - 
The quick brown fox
jumped over
the lazy dog.");
        }

        static void Test11()
        {
            // no value
            string no_value = null;
            if(no_value == null)
		    {
                Console.WriteLine("Variable 'no_value' has a value");
            }
            else
            {
                Console.WriteLine("Variable 'no_value' has no value");
            }

            // empty string
            string empty_string = "";
            if(!String.IsNullOrEmpty(empty_string))
		    {
                Console.WriteLine("Variable 'empty_string' has a value");
            }
		    else
		    {
                Console.WriteLine("Variable 'empty_string' has no value");
            }

            // white space
            string white_space = "     ";
            if(!String.IsNullOrWhiteSpace(white_space))
            {
			    Console.WriteLine("Variable 'white_space' has a value");
            }
		    else
		    {
			    Console.WriteLine("Variable 'white_space' has no value");
		    }

            // normal string
            string normal_string = "test";
            if (!String.IsNullOrWhiteSpace(normal_string))
            {
                Console.WriteLine("Variable 'normal_string' has a value");
		    }
		    else
		    {
			    Console.WriteLine("Variable 'normal_string' has no value");
		    }

            // empty list
            List<string> empty_list = new List<string>();
		    if(empty_list != null && empty_list.Count != 0)
		    {
			    Console.WriteLine("Variable 'empty_list' has a value");
		    }
		    else
		    {
			    Console.WriteLine("Variable 'empty_list' has no value");
		    }

		    // non-empty list
            List<string> non_empty_list = new List<string> { "a" };
            if (non_empty_list != null && non_empty_list.Count != 0)
            {
                Console.WriteLine("Variable 'non_empty_list' has a value");
		    }
		    else
		    {
			    Console.WriteLine("Variable 'non_empty_list' has no value");
		    }

            // empty dict
            Dictionary<string, string> empty_dict = new Dictionary<string, string>();
		    if (empty_dict != null && empty_dict.Count != 0)
		    {
			    Console.WriteLine("Variable 'empty_dict' has a value");
		    }
		    else
		    {
			    Console.WriteLine("Variable 'empty_dict' has no value");
		    }

            // non-empty dict
            Dictionary<string, string> non_empty_dict = new Dictionary<string, string> { { "a", "1" } };
            if (non_empty_dict != null && non_empty_dict.Count != 0)
            {
                Console.WriteLine("Variable 'non_empty_dict' has a value");
		    }
		    else
		    {
			    Console.WriteLine("Variable 'non_empty_dict' has no value");
		    }
        }

        class Animal
        {
            private string name;
            private string species;
                
            public Animal(string name, string species)
            {
                this.name = name;
                this.species = species;
            }

            public void Display()
            {
                Console.WriteLine($"Species: {this.species}, name: {this.name}");
            }
        }

        static void Test12()
        {
            Console.WriteLine("Test 12 - classes");

            Animal myAnimal = new Animal("Gregory", "lion");
            myAnimal.Display();
        }


        static void Test13()
        {
            Console.WriteLine("Test 13 - demonstrate nesting and white space");
            int price = 100;
            int quantity = 20;

            // If price is greater than 100 and quantity is greater than 20, discount is 10
            // If price is greater than 100 and quantity is less than or equal to 20, discount is 5
            // Otherwise if quantity is greater than 20 then discount is 3
            // Otherwise no discount
            int discount = 0;
            if (price > 100)
            {
                if (quantity > 20)
                {
                    discount = 10;
                }
                else
                {
                    discount = 5;
                }
            }
            else if (quantity > 20)
            {
                discount = 3;
            }
        }

        static void GiveMeAList(params string[] args)
        {
            foreach (string arg in args)
            {
                Console.WriteLine($"arg={arg}");
            }
        }

        static void Test14()
        {
            Console.WriteLine("Test 14 - variable arguments");

            GiveMeAList("z");
            string[] myArray = { "a", "b", "c" };
            GiveMeAList(myArray);
            // C# has no equivalent of params that accepts key/value pairs
        }

        static void CheckType(object obj)
        {
            if (obj is string)
            {
                Console.WriteLine($"{obj} is a string");
            }
            else if (obj is int)
            {
                Console.WriteLine($"{obj} is an integer");
            }
            else 
            {
                Console.WriteLine($"{obj} is some other type");
            }
        }

        static void Test15()
        {
            Console.WriteLine("Test15 - check type");
            CheckType("abc");
            CheckType(123);
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Start");
            Test1();
            Test2();
            Test3();
            Test4();
            Test5();
            Test6();
            Test7();
            Test8();
            Test9();
            Test10();
            Test11();
            Test12();
            Test13();
            Test14();
            Test15();
            Console.WriteLine("End");
        }
    }
}