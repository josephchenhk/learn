/*定义事件模型*/
public class EventCoder {

    private String Name;
    private int age;
    private double Salary;

    /*定义getter，setter*/
    public String getName() {
        return Name;
    }

    public int getAge() {
        return age;
    }

    public double getSalary() {
        return Salary;
    }

    public void setName(String name) {
        Name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void setSalary(double salary) {
        Salary = salary;
    }
}
