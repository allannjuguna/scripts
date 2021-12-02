class Shape{
	//Class variable
	String name;

	//Creating the constructor for Shape class
	Shape(){
		// System.out.println("Shape class has been created");
	}

	public String getName(String name){
		System.out.println("Current Shape : "+name);
		return name;
	}

	void getArea(double area){
		System.out.println("Updated Area of "+this.getClass().getName()+" = "+area);
	}

}





// Square
class Square extends Shape{
	double side;
	Square(double s,String n){
		super.getName(n);
		this.side=s;
		// System.out.println("Current Shape : Square Class");
	}

	void getArea(){
		double area=side * side;
		super.getArea(area);
	}
}




class Circle extends Shape{
	double radius;

	Circle(double r,String n){
		super.getName(n);
		this.radius=r;
		System.out.println("Current Shape : Circle Class . Radius = "+r);
	}


	public double getArea(){
		double area=radius * radius * (22/7);
		System.out.println("Area of circle: "+area);
		super.getArea(area);
		return area;
	}

}	


// Cylinder 
class Cylinder extends Circle{

	double height;

	Cylinder(double h,double r,String n){
		super(r,n);
		// System.out.println("Current Shape : Cylinder Class");
		this.height=h;
	}

	void getVolume(){
		double volume=super.getArea()*height;
		// System.out.println("Volume : "+volume);
		super.getArea(volume);
	}


}


class Sphere extends Circle{



	Sphere(double r,String n){
		super(r,n);
		// System.out.println("Current Shape : Sphere Class");

	}

	void findArea(){
		double area=super.getArea()*4;
		// System.out.println("Volume : "+volume);
		super.getArea(area);
	}
}

public class Program{
	public static void main(String[] args){
		System.out.println("Started the program\n\n");
		Circle A=new Circle(4.0,"Circle One");
		A.getArea();
		System.out.println("=========================================\n\n");



		Square B=new Square(4.0,"Square One");
		B.getArea();
		System.out.println("=========================================\n\n");



		Cylinder C=new Cylinder(8.0,9.0,"Cylinder One");
		C.getVolume();
		System.out.println("=========================================\n\n");



		Sphere D=new Sphere(4.0,"Sphere One");
		D.findArea();
		System.out.println("=========================================\n\n");
	}
} 
