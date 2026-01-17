"""
Main entry point for the KDSH 2026 Track A system
"""
from .prepare_data import prepare_narratives, prepare_test_data
from .test_setup import test_api_keys

def main():
    print("=" * 50)
    print("KDSH 2026 Track A - Narrative Reasoning System")
    print("=" * 50)

    # Test setup
    try:
        test_api_keys()
    except Exception as e:
        print(f"❌ Setup test failed: {e}")
        return

    # Prepare data
    try:
        prepare_narratives()
        prepare_test_data()
    except Exception as e:
        print(f"❌ Data preparation failed: {e}")
        return

    print("\n🎉 System ready!")
    print("Run test_single_example.py to test with sample data")

if __name__ == "__main__":
    main()