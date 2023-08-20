class Point1D:
    def __init__(self,x:float=0.0) -> None:
        self.x:float = float(x)
    
    def __str__(self) -> str:
        return f"Point1D{{x:{self.x}}}"
    
    def __repr__(self) -> str:
        return f"Point1D(class){{x(float):{self.x}}}"
 
class Point2D:
    def __init__(self,x:float=0.0,y:float=0.0) -> None:
        self.x:float = float(x)
        self.y:float = float(y)
    
    def __str__(self) -> str:
        return f"Point2D{{x:{self.x},y:{self.y}}}"
    
    def __repr__(self) -> str:
        return f"Point2D(class){{x(float):{self.x},y(float):{self.y}}}"

class Point3D:
    def __init__(self,x:float=0.0,y:float=0.0,z:float=0.0) -> None:
        self.x:float = float(x)
        self.y:float = float(y)
        self.z:float = float(z)

    def __str__(self) -> str:
        return f"Point3D{{x:{self.x},y:{self.y},z:{self.z}}}"
    
    def __repr__(self) -> str:
        return f"Point3D(class){{x:float{self.x},y:float{self.y},z:float{self.z}}}"

class Point4D:
    def __init__(self,x:float=0.0,y:float=0.0,z:float=0.0,w:float=0.0) -> None:
        self.x:float = float(x)
        self.y:float = float(y)
        self.z:float = float(z)
        self.w:float = float(w)

    def __str__(self) -> str:
        return f"Point4D{{x:{self.x},y:{self.y},z:{self.z},w:{self.w}}}"
    
    def __repr__(self) -> str:
        return f"Point4D(class){{x(float):{self.x},y(float):{self.y},z(float):{self.z},w(float):{self.w}}}"