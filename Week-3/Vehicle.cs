using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Weekly_Assesment3
{
    public class Vehicle
    {
        public virtual void Start()
        {
            Console.WriteLine("Vehicle is starting.");
        }
    }

    public class Car : Vehicle, IVehicle
    {
        public override void Start()
        {
            Console.WriteLine("Car is starting with ignition.");
        }

        public void Drive()
        {
            Console.WriteLine("Car is driving.");
        }
    }

    public class Bike : Vehicle
    {
        public override void Start()
        {
            Console.WriteLine("Bike is starting with a kick start.");
        }
    }
    //class Program
    //{
    //    static void Main()
    //    {
    //        Vehicle vehicle1 = new Car();
    //        Vehicle vehicle2 = new Bike();
    //        vehicle1.Start(); 
    //        vehicle2.Start(); 
    //        Vehicle vehicle3 = new Vehicle();
    //        vehicle3.Start();
    //    }
    //}
}