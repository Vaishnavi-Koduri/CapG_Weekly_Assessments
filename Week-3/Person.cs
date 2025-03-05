using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Weekly_Assesment3
{
    public class Person
    {
        public required string Name { get; set; }
        public int Age { get; set; }
        public virtual void GetDetails()
        {
            Console.WriteLine($"Name: {Name}, Age: {Age}");
        }
    }

    public class Student1 : Person
    {
        public int RollNo { get; set; }
        public override void GetDetails()
        {
            Console.WriteLine($"Student: {Name}, Age: {Age}, Roll No: {RollNo}");
        }
    }
    public class Teacher : Person
    {
        public required string Subject { get; set; }

        // Overriding the virtual method
        public override void GetDetails()
        {
            Console.WriteLine($"Teacher: {Name}, Age: {Age}, Subject: {Subject}");
        }
    }
    //class Program
    //{
    //    static void Main()
    //    {
    //        Person person1 = new Student { Name = "Alice", Age = 20, RollNo = 101 };
    //        person1.GetDetails(); 
    //        Person person2 = new Teacher { Name = "Mr. John", Age = 40, Subject = "Mathematics" };
    //        person2.GetDetails(); 
    //        Person person3 = new Person { Name = "Generic Person", Age = 35 };
    //        person3.GetDetails(); 
    //    }
    //}
}